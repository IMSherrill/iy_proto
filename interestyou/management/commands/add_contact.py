from interestyou.models import *
from django.core.management.base import BaseCommand
from interestyou.DaylifeAPI import *
import time
import datetime


class Command(BaseCommand):	
	def handle(self, *args, **options):
		#need an argument to import the name, array of seachterms, ID USER, whether they are important enough to be notified
		ct_name="name"
		ct_term="term"
		ct_notify = true
		#searchterm object needs to already exist because its not an argument, its a many-to-many field
		ct = Contact(name=ct_name, notify=ct_notify)
		ct.save()