# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from odbinfo import views

urlpatterns = [
    url(r'^o_server_list/', views.o_server_list, name='o_server_list'),
    url(r'^o_server_password_list/', views.o_server_password_list, name='o_server_password_list'),
    url(r'^o_oracle_user_list/', views.o_oracle_user_list, name='o_oracle_user_list'),
    url(r'o_mysql_user_list/', views.o_mysql_user_list, name='o_mysql_user_list'),
]
