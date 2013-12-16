#-------------------------------------------------------------------------------
# Name:        NobleUrl
# Purpose:
#
# Author:      Kev
#
# Created:     16/11/2013
# Copyright:   (c) Kev 2013
# Licence:     <your licence>
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
    keyword = trigger.group(2)
    try:
        bot.db.nobleurls.get(keyword, ('url'), 'keyword')
        bot.say(url(keyword))
    except KeyError:
        bot.say(keyword + ': unrecognised keyword')


@willie.module.commands('blist')
def nobleurl_list(bot, trigger):
    bot.reply("I'm sending you a private message of all available bookmarks!")
    print([key for key in bot.db.nobleurl.keys()])
    bookmarks = ', '.join(bot.db.nobleurl.keys())
    bot.msg(trigger.nick, bookmarks)


@willie.module.commands('addb')
def nobleurl_add(bot, trigger):
    #if bot.privileges[trigger.sender][trigger.nick] < OP:
     #   bot.reply('You must be an op to add keywords')
      #  return
    #else:

    key, url = trigger.group(1), trigger.group(2)

    last_id = bot.db.nobleurl.size()
    bot.db.nobleurl.update(last_id, (last_id, key, url), 'id')
    bot.reply('Added {}: {}'.format(key, url))

