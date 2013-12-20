#-------------------------------------------------------------------------------
# Name:        Autovoice
# Purpose:     Automatically set user mode to +v when they join the channel.
#
# Author:      Kevin Laurier
#
# Created:     16/11/2013
# Copyright:   (c) Kevin Laurier 2013
# Licence:     Eiffel Forum License v2
#-------------------------------------------------------------------------------

from willie.module import rule, event

@event('JOIN')
@rule(r'.*')
def autovoice(bot, trigger):
    channel = trigger.sender
    nick = trigger.nick
    bot.write(['MODE', channel, "+v", nick])
