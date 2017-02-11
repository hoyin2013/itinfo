from django.shortcuts import render, render_to_response
from oportmap.models import OWanIp, OLanIp, OMaps


def lan_list(request):
    user = request.user.get_username()
    if user != 'liuhui' and user != 'zhangcy' and user != 'admin':
        return render_to_response('permission_error.html')

    show_portmap = request.session.get('show_portmap')

    lan_lists = OLanIp.objects.all()
    return render_to_response('oportmap/lan_list.html', locals())


def wan_list(request):
    user = request.user.get_username()
    print(user)
    if user != 'liuhui' and user != 'zhangcy' and user != 'admin':
        return render_to_response('permission_error.html')

    show_portmap = request.session.get('show_portmap')

    wan_lists = OWanIp.objects.all()
    return render_to_response('oportmap/wan_list.html', locals())


def map_list(request):
    user = request.user.get_username()
    if user != 'liuhui' and user != 'zhangcy' and user != 'admin':
        return render_to_response('permission_error.html')

    show_portmap = request.session.get('show_portmap')

    map_lists = OMaps.objects.all()
    return render_to_response('oportmap/map_list.html', locals())
