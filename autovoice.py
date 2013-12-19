from willie.module import rule, event

@event('JOIN')
@rule(r'.*')
def autovoice(bot, trigger):
    channel = trigger.sender
    nick = trigger.nick
    bot.write(['MODE', channel, "+v", nick])
