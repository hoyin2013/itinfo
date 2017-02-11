# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from dbinfo import views

urlpatterns = [
    url(r'^server_list/', views.server_list, name='server_list'),
    url(r'^server_password_list/', views.server_password_list, name='server_password_list'),
    url(r'^oracle_user_list/', views.oracle_user_list, name='oracle_user_list'),
    url(r'mysql_user_list/', views.mysql_user_list, name='mysql_user_list'),
]
