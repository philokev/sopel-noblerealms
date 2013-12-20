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
        nobleurl_table = ('who', ('id', 'nick', 'desc'), 'id')
        if not bot.db.check_table(*nobleurl_table):
            bot.db.add_table(*nobleurl_table)


@willie.module.commands('n', 'who', 'about')
def who(bot, trigger):
    nick = trigger.group(2)
    try:
        desc = bot.db.who.get(nick, ('desc'), 'nick')
        bot.say(desc)
    except KeyError:
        bot.say('{} : unrecognised nickname'.format(nick))


@willie.module.commands('listn')
def nickname_list(bot, trigger):
    bot.reply("I'm sending you a private message of all available nicknames!")
    bookmarks = ', '.join(nick[0] for nick in bot.db.who.keys('nick'))
    bot.msg(trigger.nick, bookmarks)


@willie.module.commands('addn')
def nickname_add(bot, trigger):
    if bot.privileges[trigger.sender][trigger.nick] >= OP:
        nick, desc = trigger.group(2).split(' ', 1)
        nick = nick.lower()
        last_id = str(bot.db.who.size())
        bot.db.who.update(last_id, {'id': last_id, 'nick': nick, 'desc': desc}, 'id')
        bot.reply('Added {}: {}'.format(nick, desc))
    else:
        bot.reply('You must be an op to add nickname descriptions')         


@willie.module.commands('deln')
def nickname_del(bot, trigger):
    if bot.privileges[trigger.sender][trigger.nick] >= OP:
        nick = trigger.group(2).lower()
        bot.db.who.delete(nick, 'nick')
        bot.reply('Removed {}'.format(nick))
    else:
        bot.reply('You must be an op to add nickname descriptions')
        
        
@willie.module.commands('desc')
def desc(bot, trigger):
        desc = trigger.group(2)
        last_id = str(bot.db.who.size())
        if bot.db.who.contains():
            bot.db.who.update(nick, {'desc': desc}, 'nick')
        else:
            bot.db.who.update(last_id, {'id': last_id, 'nick': nick, 'desc': desc}, 'id')
        
        bot.reply('Added {}: {}'.format(nick, desc))