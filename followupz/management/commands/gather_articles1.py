from followupz.models import *
from django.core.management.base import BaseCommand
from followupz.DaylifeAPI import *
import time
import datetime


class Command(BaseCommand):	
	def handle(self, *args, **options):
		api = DaylifeAPI("03e38ae349885745226680ad7140212b", "c07ea3fe4284ae87bf032c6e12174e15", "freeapi.daylife.com")
		#grab contact list
		contacts = Contact.objects.all()
		for contact in contacts:
			#search API for articles relating to the first searchterm
			ret = api.search_getRelatedArticles(query=contact.searchTerms.all()[0].term, start_time=long(time.time() - (7*86400)), end_time=long(time.time()), sort="date")
			#grab art date from article
			art_date = DateTime.parse(ret['response']['payload']['article'][0]['timestamp'])
			#populate the article object 
			article = Article(pub_date= art_date, headline=ret['response']['payload']['article'][0]['headline'], blurb=ret['response']['payload']['article'][0]['excerpt'], url=ret['response']['payload']['article'][0]['url'], publication=ret['response']['payload']['article'][0]['source']['name'])
			article.save()
			#make a variable for term
			current_term = contact.searchTerms.all()[0]
			current_term.save()
			#update article to the corresponding search term
			current_term.articles.add(article)
			#save search term so its updated in database with new article
			current_term.save()