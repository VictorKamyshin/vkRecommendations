# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render
from vkApp.forms import AuthorisationForm
from django.http import HttpResponseRedirect
import vk
# Create your views here.


def my_view(request):
    auth_form = AuthorisationForm
    return render(request,'auth.html',{'form':auth_form})


def auth(request):
    if request.method == 'POST':
        print "get post"
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            session = vk.AuthSession(app_id=6180230,user_login=username,user_password=password)
            api = vk.API(session)
            return HttpResponse("Successfully authorised")
        except :
            return HttpResponseRedirect('/authorisation')
    return HttpResponse("Hello World!")