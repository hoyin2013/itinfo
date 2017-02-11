# -*- coding: utf-8 -*-

from django.conf.urls import url
from shortcut import views

urlpatterns = [
    url(r'^shortcut_list/', views.shortcut_list, name='shortcut_list'),
]
