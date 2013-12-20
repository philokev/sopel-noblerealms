"""
Name:		Alexandria Search
Purpose:	Customised version of the calibre module to search the Alexandria library
Author:	  	Kevin Laurier
Created:	14/11/2013
Copyright:	(c) Kevin Laurier 2013
Licence:	Eiffel Forum License v2
"""


from base64 import b64encode
import requests
from willie.module import commands, example


class CalibreRestFacade(object):
	"""
	Connect to Calibre using its REST api
	"""
	def __init__(self, url, username, password):
		"""
		Initialize a connection to Calibre using the Requests library
		"""
		self.url = url
		self.username = username
		self.password = password
		self.auth = requests.auth.HTTPDigestAuth(username, password)

	def books(self, book_ids):
		"""
		Get all books corresponding to a list of IDs
		"""
		book_ids_csv = ','.join(str(b_id) for b_id in book_ids)
		return requests.get(self.url + '/ajax/books', 
			auth=self.auth, params={'ids': book_ids_csv}).json()

	def search(self, keywords):
		"""
		Get a list of IDs corresponding to the search results
		"""
		return requests.get(self.url + '/ajax/search', 
			auth=self.auth, params={'query': keywords}).json()


def configure(config):
	"""
	| [calibre] | example | purpose |
	| ---------- | ------- | ------- |
	| url | http://localhost:8080 | The URL to Alexandria |
	| username | calibre | The username used to log on Alexandria (if any) |
	| password | password | The password used to log on Alexandria (if any) |
	"""
	if config.option('Configure Alexandria', False):
		if not config.has_section('alexandria'):
			config.add_section('alexandria')
		config.interactive_add('alexandria', 'url', "Enter the URL to your Calibre server (without trailing slashes)")
		
		if config.option('Configure username / password for Alexandria?'):
			config.interactive_add('alexandria', 'username', "Enter your Alexandria username")
			config.interactive_add('alexandria', 'password', "Enter your Alexandria password", ispass=True)
		config.save()		


def setup(bot):
	a = bot.config.alexandria
	bot.memory['alexandria'] = CalibreRestFacade(a.url, a.username, a.password)


@commands('alexandria', 'alex')
@example('.alexandria gods of eden')
@example('.alex')
def alexandria(bot, trigger):
	"""
	Queries a configured Calibre library and returns one or more URLs
	corresponding to the search results. If no search words are entered,
	the URL of the Calibre server will be returned.
	"""
	search_words = trigger.group(2)
	if not search_words:
		bot.reply('The Calibre library is here: ' + bot.config.alexandria.url)
		return
		
	calibre = bot.memory['alexandria']
	book_ids = calibre.search(search_words)['book_ids']
	num_books = len(book_ids)

	if num_books == 1:
		book_title = calibre.books(book_ids).values()[0]['title']
		bot.reply(u'{}: {}/browse/book/{}'
			.format(book_title, calibre.url, book_ids[0]))				

	elif num_books > 1:
		results = calibre.books(book_ids)
		books = [(book_id, results[str(book_id)]) for book_id in book_ids]

		bot.reply("I'm sending you a private message of all Alexandria search results!")
		bot.msg(trigger.nick, "{} results for '{}'"
			.format(len(books), search_words))

		for book_id, book in books:
			bot.msg(trigger.nick, u'{}: {}/browse/book/{}'
				.format(book['title'], calibre.url, book_id))
	else:
		bot.say("Alexandria: No results found.")


@commands('alexinfo')
def alexinfo(bot, trigger):
	bot.say('URL: ' + bot.config.alexandria.url)
	bot.say('Username: ' + bot.config.alexandria.username)
	bot.say('Password: ' + bot.config.alexandria.password)
