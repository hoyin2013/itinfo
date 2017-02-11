# -*- coding: utf-8 -*-

from django.conf.urls import url
from ipresource import views

urlpatterns = [
    url(r'^ip_list/', views.ip_list, name='ip_list'),
    url(r'^pos_list/', views.pos_list, name='pos_list'),
]
