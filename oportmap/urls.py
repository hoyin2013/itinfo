# -*- coding: utf-8 -*-

from django.conf.urls import url
from oportmap import views

urlpatterns = [
    url(r'^lan_list/', views.lan_list, name='lan_list'),
    url(r'^wan_list/', views.wan_list, name='wan_list'),
    url(r'^map_list/', views.map_list, name='map_list'),
]