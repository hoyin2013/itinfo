# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, render
from django.contrib import auth
from django.http.response import HttpResponseRedirect


def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        # print(password)
        user = auth.authenticate(username=name, password=password)
        print(user)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['username'] = name

            return HttpResponseRedirect('/index')
        else:
            return render_to_response("ok.html", {'result': '用户名或密码错误!'})
    return render(request,'login.html')


def auth_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login')


def index(request):
    username = request.session.get('username')
    if username is None:
        return HttpResponseRedirect('/login')

    return render_to_response('index.html', locals())


def test(request):
    return render_to_response("test.html", {})
