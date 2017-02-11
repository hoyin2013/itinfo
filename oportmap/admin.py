# -*- coding: utf-8 -*-
from django.contrib import admin
from oportmap.models import OWanIp, OLanIp, OMaps


@admin.register(OWanIp)
class WanIpAdmin(admin.ModelAdmin):
    list_display = ('id', 'w_ip', 'description')


@admin.register(OLanIp)
class LanIpAdmin(admin.ModelAdmin):
    list_display = ('id', 'l_ip', 'area', 'status', 'description')


@admin.register(OMaps)
class MapsAdmin(admin.ModelAdmin):
    list_display = ('id', 'w_ip', 'w_port', 'l_ip', 'l_port','map_user', 'map_date', 'description')

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        def __init__(self):
            pass

        js = (
            '/static/js/My97DatePicker/WdatePicker.js' ,
        )
