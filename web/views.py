# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# from django.http import JsonResponse
# from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def template(req):
    return render(req, 'template.html', context={"status":"ok"})
    # HttpResponse("SALAM")