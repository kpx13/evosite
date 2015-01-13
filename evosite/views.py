# -*- coding: utf-8 -*-

from django.core.context_processors import csrf
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from pages.models import Page
from feedback.models import Feedback
import config

@csrf_exempt
def page(request, page_name):
    c = {}
    c['request_url'] = page_name
    c['is_debug'] = settings.DEBUG
    c.update(csrf(request))
    p = Page.get_by_slug(page_name)
    if not p:
        raise Http404()
    if request.method == "POST":
        Feedback(
            name=request.POST.get('name', '?'),
            email=request.POST.get('email', '?'),
            text=request.POST.get('text', '?')).save()
    c['p'] = p
    return render_to_response('page.html', c, context_instance=RequestContext(request))