# -*- coding: utf-8 -*-

from django.conf.urls import url
from issues import views

urlpatterns = [
    url(r'^event_list/', views.event_list, name='event_list'),
    url(r'^system_list/', views.system_list, name='system_list'),
    url(r'^person_list/', views.person_list, name='person_list'),
]
