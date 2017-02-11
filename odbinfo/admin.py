# -*- coding:utf-8 -*-
from django.contrib import admin
from odbinfo.models import Odbserver, Ousers, Omysqluser, Osysusers


@admin.register(Odbserver)
class DbserverAdmin(admin.ModelAdmin):
    search_fields = ['name', 'ip', 'pos']

    list_display = ('name', 'ip', 'pos','sn', 'sid', 'firm', 'model', 'feature', 'buy_time', 'service_range', 'comment')


@admin.register(Ousers)
class UsersAdmin(admin.ModelAdmin):
    search_fields = ['user', 'status']

    list_display = ['dbserver','user', 'passwd', 'tablespace', 'status', 'business', 'created', 'comment']


@admin.register(Omysqluser)
class MysqluserAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('dbserver', 'name', 'passwd', 'dbname', 'business', 'comment')


@admin.register(Osysusers)
class SysusersAdmin(admin.ModelAdmin):
    list_display = ('dbserver', 'name', 'user', 'passwd')
