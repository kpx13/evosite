# encoding: utf-8
from django.conf import settings
from django.core.mail import send_mail
from livesettings import config_value

def sendmail(subject, body, to_email=None):
    if not to_email:
        to_email = config_value('MyApp', 'EMAIL')
    mail_subject = ''.join(subject)
    send_mail(mail_subject, unicode(body.replace('&quot;', u'"')), settings.DEFAULT_FROM_EMAIL, [to_email])