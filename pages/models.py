# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
import pytils
from dashboard import string_with_title

class Page(models.Model):
    title = models.CharField(max_length=256, verbose_name=u'заголовок')
    slider = RichTextField(blank=True, verbose_name=u'часть со слайдером')
    content = RichTextField(blank=True, verbose_name=u'содержимое')
    slug = models.SlugField(verbose_name=u'url', unique=True, blank=True, help_text=u'Заполнять не нужно')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=pytils.translit.slugify(self.title)
        super(Page, self).save(*args, **kwargs)
    
    @staticmethod
    def get_by_slug(page_name):
        try:
            return Page.objects.get(slug=page_name)
        except:
            return None
        
    class Meta:
        verbose_name = u'статическая страница'
        verbose_name_plural = u'статические страницы'
        app_label = string_with_title("pages", u"Статические страницы")
        ordering=['slug']
        
    def __unicode__(self):
        return self.slug
