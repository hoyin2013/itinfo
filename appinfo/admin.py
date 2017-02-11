# -*- coding:utf-8 -*-

from django.contrib import admin
from appinfo.models import Server, Deploy, App, Business


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    search_fields = ['name', ]

    list_display = [
        'name', 'ip', 'zone', 'sn', 'sid', 'manufacturer', 'mod', 'type', 'feature',
        'buy_date', 'contact', 'factory_phone', 'service_range', 'cabinet', 'idc', 'comment']

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        def __init__(self):
            pass

        js = (
            '/static/js/My97DatePicker/WdatePicker.js' ,
        )


@admin.register(Deploy)
class DeployAdmin(admin.ModelAdmin):
    search_fields = ['name', ]

    list_display = [
        'name', 'server', 'app', 'paths', 'users', 'ports', 'documents', 'author', 'dtime']


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    search_fields = ['name', ]

    list_display = [
        'name', 'language', 'function', 'teams', 'dev_time', 'contact', 'comment']


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    search_fields = ['name', ]

    list_display = ['name', 'description', 'contacts', 'ol_date', 'deploy_list', 'details', 'annex']

    def preview(self, obj):
        return '<a href="/uploads/%s"  target="_blank"><img src="/uploads/%s" height="64" width="64" /></a>' % (
            obj.architecture, obj.architecture)

    preview.allow_tags = True
    preview.short_description = "架构图"

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        def __init__(self):
            pass

        js = (
            'js/editor/kindeditor-4.1.10/kindeditor-all.js',
            'js/editor/kindeditor-4.1.10/lang.zh_CN.js',
            'js/editor/kindeditor-4.1.10/config.js',
        )
