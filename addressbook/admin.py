# -*- coding:utf-8 -*-
from django.contrib import admin
from addressbook.models import Company, Persons


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    list_display = ['name', 'address', 'tel', 'website', 'comments']


@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    search_fields = ['name', 'dept', ]
    ordering = ['dept', 'name']

    def agenda(self, obj):
        if obj.sex:
            return "男"
        elif not obj.sex:
            return "女"
        else:
            return "未知"

    agenda.short_description = "性别"
    agenda.allow_tags = True

    fields = ['name', 'sex', 'dept', 'contact', 'company', 'comment']
    list_display = ['name', 'agenda', 'dept', 'contact','company', 'comment']
