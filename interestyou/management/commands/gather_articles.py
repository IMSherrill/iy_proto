from interestyou.models import *
from django.core.management.base import NoArgsCommand
from interestyou.DaylifeAPI import *
import time
import datetime
import dateutil.parser


class Command(NoArgsCommand):	
	def handle_noargs(self, **options):
		api = DaylifeAPI("03e38ae349885745226680ad7140212b", "c07ea3fe4284ae87bf032c6e12174e15", "freeapi.daylife.com")
		#grab searchTerm list
		st = SearchTerm.objects.all()
		for current_term in st:
			# Search API for articles relating to current_term
			ret = api.search_getRelatedArticles(query=current_term.term, start_time=long(time.time() - (7*86400)), end_time=long(time.time()), sort="date")
			for a in range(5):
				# Grab art date from article so I can convert it to a readable format
				art_date = dateutil.parser.parse(ret['response']['payload']['article'][a]['timestamp'])
				# Parse article			
				article = Article(pub_date= art_date, headline=ret['response']['payload']['article'][a]['headline'], blurb=(ret['response']['payload']['article'][a]['excerpt'])[:50], url=(ret['response']['payload']['article'][a]['url'])[:199], publication=ret['response']['payload']['article'][a]['source']['name'])
				# If the current article doesn't already exist, store it in the DB.
				if not Article.objects.filter(url=article.url):
					article.save()
					# Add article object to appropriate searchterm
					current_term.articles.add(article)
					current_term.save()