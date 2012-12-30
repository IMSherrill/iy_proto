from followupz.models import *
from django.core.management.base import NoArgsCommand
from followupz.DaylifeAPI import *
import time
import datetime
import smtplib
import string
from django.template.loader import render_to_string


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
# 			#uses smtplib for emailing
# 			SUBJECT = "Follow Upz Reminder"
# 			TO = current_user.email
# 			FROM = "notifier@fz.com"
# 			text = email_text
# 			BODY = string.join((
#         		"From: %s" % FROM,
#         		"To: %s" % TO,
#         		"Subject: %s" % SUBJECT ,
#         		"",
#         		text
#         		), "\r\n")
# 			server = smtplib.SMTP(HOST)
# 			server.sendmail(FROM, [TO], BODY)
# 			server.quit()