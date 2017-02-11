# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response

from models import Odbserver, Ousers, Osysusers, Omysqluser
from datetime import date, datetime


def o_server_list(request):
    user = request.user.get_username()
    if user != 'yinhb' and user != 'denghui' and user != 'admin':
        return render_to_response('permission_error.html')
    server_lists = Odbserver.objects.all()
    for server in server_lists:
        btime = server.buy_time
        yeard = server.service_range
        if btime is None:
            server.buy_time = 0
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

    return render_to_response('odbinfo/server_list.html', locals())


def o_server_password_list(request):
    user = request.user.get_username()
    if user != 'yinhb' and user != 'denghui' and user != 'admin':
        return render_to_response('permission_error.html')

    sysuser_lists = Osysusers.objects.all()
    return render_to_response('odbinfo/server_password.html', locals())


def o_oracle_user_list(request):
    user = request.user.get_username()
    if user != 'yinhb' and user != 'denghui' and user != 'admin':
        return render_to_response('permission_error.html')

    user_lists = Ousers.objects.all()
    return render_to_response('odbinfo/ouser_list.html', locals())


def o_mysql_user_list(request):
    user = request.user.get_username()
    if user != 'yinhb' and user != 'denghui' and user != 'admin':
        return render_to_response('permission_error.html')

    mysql_lists = Omysqluser.objects.all()
    return render_to_response('odbinfo/mysql_list.html',locals())