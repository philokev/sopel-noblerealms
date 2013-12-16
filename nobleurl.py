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

KEYWORDS = {
    'montalk': 0,

    'cassiopaea': 1,
    'cassiopaeans': 1,
    'cass': 1,

    'botd': 2,
    'pleiadians': 2,
    'bringer': 2,

    'bibliotecapleyades': 3,
    'bib': 3,

    'kjv': 4,

    'soul': 5,

    'blackfox': 6,

    'bitcoin': 7,

    'haich': 8
}

NR_URLS = [
    'http://www.montalk.net',
    'https://cassiopaea.org/forum/index.php/topic,13581.0.html',
    'http://www.universe-people.com/english/svetelna_knihovna/htm/en/en_kniha_bringers_of_the_dawn.htm',
    'http://www.bibliotecapleyades.net',
    'http://www.kingjamesbibleonline.org/',
    'http://soul1.org/Rainbow_bridge2.htm',
    'http://brain.wireos.com',
    'https://www.weusecoins.com',
    'http://www.znakovi-vremena.net/en/Elisabeth_Haich_Initiation.pdf'
]

@willie.module.commands('url', 'link', 'b')
def nobleurl(bot, trigger):
    keyword = trigger.group(2)
    try:
        bot.say(url(keyword))
    except KeyError:
        bot.say(keyword + ': unrecognised keyword')


@willie.module.commands('blist')
def nobleurl_list(bot, trigger):
    bot.reply("I'm sending you a private message of all available bookmarks!")
    bookmarks = ', '.join(key for key, _ in sorted(KEYWORDS.items(), key=itemgetter(1)))
    bot.msg(trigger.nick, bookmarks)


def url(keyword):
    return NR_URLS[KEYWORDS[keyword]]
