# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from portmap.models import WanIp, LanIp, Maps, Vagent, BankTunnel


def lan_list(request):
    user = request.user.get_username()
    print(user)
    if user != 'liuhui' and user != 'zhangcy' and user != 'admin':
        return render_to_response('permission_error.html')

    lan_lists = LanIp.objects.all()
    return render_to_response('portmap/lan_list.html', locals())


def wan_list(request):
    user = request.user.get_username()
    if user != 'liuhui' and user != 'zhangcy' and user != 'admin':
        return render_to_response('permission_error.html')

    show_portmap = request.session.get('show_portmap')

    wan_lists = WanIp.objects.all()
    return render_to_response('portmap/wan_list.html', locals())


def map_list(request):
    user = request.user.get_username()
    if user != 'liuhui' and user != 'zhangcy' and user != 'admin':
        return render_to_response('permission_error.html')

    show_portmap = request.session.get('show_portmap')

    map_lists = Maps.objects.all()
    return render_to_response('portmap/map_list.html', locals())


def agent_list(request):
    user = request.user.get_username()
    if user != 'liuhui' and user != 'zhangcy' and user != 'admin':
        return render_to_response('permission_error.html')

    show_portmap = request.session.get('show_portmap')

    vagent_lists = Vagent.objects.all()
    return render_to_response('portmap/agent_list.html', locals())


def tunnel_list(request):
    user = request.user.get_username()
    if user != 'liuhui' and user != 'zhangcy' and user != 'admin':
        return render_to_response('permission_error.html')

    tunnel_lists = BankTunnel.objects.all()
    return render_to_response('portmap/union_list.html', locals())
