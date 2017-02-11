# -*- coding: utf-8 -*-

from django.conf.urls import url
from addressbook import views

urlpatterns = [
    url(r'^company_list/', views.company_list, name='company_list'),
    url(r'^person_list/', views.person_list, name='person_list'),
]
