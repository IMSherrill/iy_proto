from interestyou.models import *
from django.core.management.base import NoArgsCommand
from interestyou.DaylifeAPI import *
import time
import datetime
import smtplib
import string
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

class Command(NoArgsCommand):
	def handle_noargs(self, **options):
		#grab user list
		ulist = User.objects.all()
		#go through user list sends email to notify and maybe also updates some account page on the website
		for current_user in ulist:
			#get the list of this users contacts
			clist = Contact.objects.filter(user=current_user)
			email_text = render_to_string('email-update.html', {'contacts' : clist})
			print email_text
 			#uses smtplib for emailing
 			msg = EmailMultiAlternatives('interestyou Reminder', email_text, 'imsherrill@gmail.com',
    [current_user.email])
    		msg.attach_alternative(email_text, "text/html")
    		msg.send()
