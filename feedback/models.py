# -*- coding: utf-8 -*-
from django.db import models
from dashboard import string_with_title
from sendmail import sendmail

class Feedback(models.Model):
    name = models.CharField(u'Имя', blank=True, max_length=255)
    email = models.CharField(u'Email', blank=True, max_length=255)
    text = models.TextField(u'Текст сообщения')
    request_date = models.DateTimeField(u'дата заявки', auto_now_add=True)
                    
    class Meta:
        verbose_name = u'сообщение'
        verbose_name_plural = u'обратная связь'
        ordering = ['-request_date']
        app_label = string_with_title("feedback", u"Обратная связь")

    def __unicode__(self):
        return self.email

    def save(self, *args, **kwargs):
        super(Feedback, self).save(*args, **kwargs)
        sendmail(u'Новое сообщение от эвомейлинга', u"""
Имя: %s
Email: %s
Текст: %s
""" % (self.name, self.email, self.text))
