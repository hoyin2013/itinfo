from django.shortcuts import render_to_response
from ipresource.models import Pos, Ipaddr


def ip_list(requests):
    ip_lists = Ipaddr.objects.all()
    return render_to_response('ipresource/ip_list.html', locals())


def pos_list(requests):
    pos_lists = Pos.objects.all()
    return render_to_response('ipresource/pos_list.html', locals())