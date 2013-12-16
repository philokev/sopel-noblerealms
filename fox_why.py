from willie.module import rule

@rule('(?i).*(who|what|why).*(fox|fox_|goldmember|fox_mulder).*$')
def fox_why(bot, trigger):
    bot.reply("fox_/fox/goldmember was banned for inappropiate behavior in the past from having 5 prior bans. He was spreading rumors, couldn\'t back his sources, was disinfo and had rude behavior.")
