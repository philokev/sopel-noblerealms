#-------------------------------------------------------------------------------
# Name:        NobleUrl
# Purpose:     Associate a URL to a keyword.
#
# Author:      Kevin Laurier
#
# Created:     16/11/2013
# Copyright:   (c) Kevin Laurier 2013
# Licence:     Eiffel Forum License v2
#-------------------------------------------------------------------------------

from operator import itemgetter
import willie
from willie.module import commands, OP

def setup(bot):
    if bot.db:
        nobleurl_table = ('nobleurl', ('id', 'keyword', 'url'), 'id')
        if not bot.db.check_table(*nobleurl_table):
            bot.db.add_table(*nobleurl_table)


@willie.module.commands('url', 'link', 'b')
def nobleurl(bot, trigger):
    keyword = trigger.group(2).lower()
    try:
        url = bot.db.nobleurl.get(keyword, ('url'), 'keyword')
        bot.say(url)
    except KeyError:
        bot.say(keyword + ': unrecognised keyword')


@willie.module.commands('listb')
def nobleurl_list(bot, trigger):
    bot.reply("I'm sending you a private message of all available bookmarks!")
    bookmarks = ', '.join(key[0] for key in bot.db.nobleurl.keys('keyword'))
    bot.msg(trigger.nick, bookmarks)


@willie.module.commands('addb')
def nobleurl_add(bot, trigger):
    if bot.privileges[trigger.sender][trigger.nick] < OP:
        bot.reply('You must be an op to add keywords')
        return
    else:
        key, url = trigger.group(2).split(' ')
        key = key.lower()
        last_id = str(bot.db.nobleurl.size())
        bot.db.nobleurl.update(last_id, {'id': last_id, 'keyword': key, 'url': url}, 'id')
        bot.reply('Added {}: {}'.format(key, url))


@willie.module.commands('delb')
def nobleurl_del(bot, trigger):
    if bot.privileges[trigger.sender][trigger.nick] < OP:
        bot.reply('You must be an op to add keywords')
        return
    else:
        key = trigger.group(2).lower()
        bot.db.nobleurl.delete(key, 'keyword')
        bot.reply('Removed {}'.format(key))