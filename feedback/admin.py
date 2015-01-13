# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text', 'request_date',)
    ordering = ('request_date', )

admin.site.register(Feedback, FeedbackAdmin)