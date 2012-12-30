from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	send_emails = models.BooleanField(default=True)

class SearchTerm(models.Model):
	term = models.CharField(max_length=200)
	articles = models.ManyToManyField('Article')

class Article(models.Model):
	pub_date = models.DateTimeField('date published')
	headline = models.CharField(max_length=200)
	blurb = models.CharField(max_length=4000)
	url = models.URLField()
	publication = models.CharField(max_length=200)

class Contact(models.Model):
	name = models.CharField(max_length=200)
	notify = models.BooleanField(default=True)
	user = models.ForeignKey(User)
	searchTerms = models.ManyToManyField(SearchTerm)
	articles = models.ManyToManyField('Article', through='Suggestion')

class Suggestion(models.Model):
	contact = models.ForeignKey(Contact)
	article = models.ForeignKey(Article)
	was_shown = models.BooleanField(default=False)

