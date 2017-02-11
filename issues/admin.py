# -*- coding:utf-8 -*-
from django.contrib import admin
from issues.models import System, Person, Event


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'dept', 'mobile', 'email', 'comment')


@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ('sname', 'short_desc', 'author', 'comment')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('release', 'title', 'sponsor', 'sp_dept', 'update_type', 'project', 'operator', 'op_type',
                    'begin_time', 'end_time')
