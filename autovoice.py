from willie.module import event

@event('JOIN')
@rule(r'.*')
def autovoice(bot, trigger):
    bot.write(['MODE', channel, "+v", trigger.nick])
