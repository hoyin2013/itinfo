# -*- coding: utf-8 -*-
from django.contrib import admin
from portmap.models import WanIp, LanIp, Maps, Agent, BankTunnel


@admin.register(WanIp)
class WanIpAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'w_ip',
                    'description'
                    )


@admin.register(LanIp)
class LanIpAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'l_ip',
                    'area',
                    'status',
                    'description'
                    )


@admin.register(Maps)
class MapsAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'w_ip',
                    'w_port',
                    'l_ip',
                    'l_port',
                    'map_user',
                    'map_date',
                    'description'
                    )


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'agent_ip',
                    'agent_port',
                    'app_ip',
                    'app_port',
                    'description'
                    )


@admin.register(BankTunnel)
class BankTunnelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',
                    'bank_ip',
                    'local_ip',
                    'bank_contact',
                    'local_contact',
                    'tech_contact',
                    'open_date',
                    'script',
                    'description'
                    )

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        def __init__(self):
            pass

        js = (
            '/static/js/My97DatePicker/WdatePicker.js' ,
        )
