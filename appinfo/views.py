# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from .models import Server, Business, App, Deploy
from datetime import date, datetime


def server_list(request):
    server_lists = Server.objects.all()
    for server in server_lists:
        btime = server.buy_date
        yeard = server.service_range
        if btime is None:
            server.buy_date = 0
        else:
            y = int(btime.year)
            m = str(btime.month)
            d = str(btime.day)
            y = y + yeard
            s_expire = str(y) + '-' + m + '-' + d
            t_expire = datetime.strptime(s_expire, '%Y-%m-%d').date()

            today = date.today()
            distance = (today - t_expire).days
            if distance > 0:
                server.buy_date = 2
            else:
                server.buy_date = 1
            server.service_range = t_expire
        print(server.buy_date)

    return render_to_response('appinfo/server_list.html', locals())


def business_list(request):
    business_lists = Business.objects.all()
    return render_to_response('appinfo/business_list.html', locals())


def app_list(request):
    app_lists = App.objects.all()
    return render_to_response('appinfo/app_list.html', locals())


def deploy_list(request):
    deploy_lists = Deploy.objects.all()
    return render_to_response('appinfo/deploy_list.html', locals())