# -*- coding: utf-8 -*-

from django.conf.urls import url
from portmap import views

urlpatterns = [
    url(r'^lan_list/', views.lan_list, name='lan_list'),
    url(r'^wan_list/', views.wan_list, name='wan_list'),
    url(r'^map_list/', views.map_list, name='map_list'),
    url(r'^agent_list/', views.agent_list, name='agent_list'),
    url(r'^tunnel_list/', views.tunnel_list, name='tunnel_list'),
]