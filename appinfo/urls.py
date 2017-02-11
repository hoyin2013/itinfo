# -*- coding: utf-8 -*-

from django.conf.urls import url
from appinfo import views

urlpatterns = [
    url(r'^server_list/', views.server_list, name='server_list'),
    url(r'^app_list/', views.app_list, name='app_list'),
    url(r'^deploy_list/', views.deploy_list, name='deploy_list'),
    url(r'^business_list/', views.business_list, name='business_list'),
]
