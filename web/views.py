# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
# from django.http import JsonResponse
# from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
import re
from .models import List, Person, Word
from django.core import signing

# Create your views here.

def template(req):
    return render(req, 'template.html', context={"status":"ok"})


@csrf_exempt
def signup(req):
    if req.method == "POST":
        username = req.POST['username'] if 'username' in req.POST else ''
        password = req.POST['password'] if 'password' in req.POST else ''
        repassword = req.POST['repassword'] if 'repassword' in req.POST else ''
        lang = req.POST['langselect'] if 'langselect' in req.POST else ''
        email = req.POST['email'] if 'email' in req.POST else ''
        dic = {}
        # validation
        flag = True
        if not re.match('^[0-9a-zA-Z_]{4,24}$', username):
            flag = False
            dic['username'] = 'Username must be form of [0-9a-zA-Z_] with length at least 4 at last 24 character'
        if lang == '0':
            flag = False
            dic['lang'] = 'Select your language :)'
        if not re.match('^[0-9a-zA-Z_]{4,24}$', password):
            flag = False
            dic['password'] = 'Password must be form of [0-9a-zA-Z_] with length at least 4 at last 24 character'
        if not re.match('^[0-9a-zA-Z_]{4,24}$', repassword):
            flag = False
            dic['repassword'] = 'Password repeat must be form of [0-9a-zA-Z_] with length at least 4 at last 24 character'
        if password != repassword:
            flag = False
            dic['pass_eq_repass'] = 'Password is not equal with passwordrepeat'
        if not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            flag = False
            dic['email'] = 'Email is not valid'
        if Person.objects.filter(user_name=username).exists():
            flag = False
            dic['unameTekrari'] = 'Username is already exists'
        # end validation
        if flag == True:
            dic['ok'] = "Signed up successfully"
        if flag == False:
            return render(req, 'signup.html', context=dic)
        else:
            Person.objects.create(user_name=username, user_password=signing.dumps(password), email=signing.dumps(email),language=lang)
            return render(req, 'signup.html', context=dic)
    else:
        return render(req, 'signup.html', context={})
        # return HttpResponseRedirect("/admin/")
        
@csrf_exempt
def signin(req):
    return render(req, 'signin.html', context={})