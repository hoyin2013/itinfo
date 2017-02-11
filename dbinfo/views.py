# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response

from models import Dbserver, Users, Sysusers, Mysqluser
from datetime import date, datetime


def server_list(request):
    user = request.user.get_username()
    if user != 'yinhb' and user != 'denghui' and user != 'admin':
        return render_to_response('permission_error.html')
    server_lists = Dbserver.objects.all()
    for server in server_lists:
        btime = server.buy_time
        yeard = server.service_range
        if btime is None:
            server.buy_time = 0
            server.service_range = '未知'
        else:
            y = int(btime.year)
            m = str(btime.month)
            d = str(btime.day)
            y = y + yeard
            s_expire = str(y) + '-' + m + '-' + d
            t_expire = datetime.strptime(s_expire, '%Y-%m-%d').date()

            print(t_expire)
            today = date.today()
            distance = (today - t_expire).days
            if distance > 0:
                server.buy_time = 2
            else:
                server.buy_time = 1
            server.service_range = t_expire

    return render_to_response('dbinfo/server_list.html', locals())


def server_password_list(request):
    user = request.user.get_username()
    if user != 'yinhb' and user != 'denghui' and user != 'admin':
        return render_to_response('permission_error.html')

    sysuser_lists = Sysusers.objects.all()
    return render_to_response('dbinfo/server_password.html', locals())


def oracle_user_list(request):
    user = request.user.get_username()
    if user != 'yinhb' and user != 'denghui' and user != 'admin':
        return render_to_response('permission_error.html')

    user_lists = Users.objects.all()
    return render_to_response('dbinfo/ouser_list.html', locals())


def mysql_user_list(request):
    user = request.user.get_username()
    if user != 'yinhb' and user != 'denghui' and user != 'admin':
        return render_to_response('permission_error.html')

    mysql_lists = Mysqluser.objects.all()
    return render_to_response('dbinfo/mysql_list.html',locals())