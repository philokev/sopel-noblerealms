from willie.module import event

@event('JOIN')
def autovoice(bot, trigger):
    bot.write(['MODE', channel, "+v", trigger.nick])
