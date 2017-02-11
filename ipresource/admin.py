from django.contrib import admin
from ipresource.models import Ipaddr,Pos

# Register your models here.
@admin.register(Ipaddr)
class IpaddrAdmin(admin.ModelAdmin):
    search_fields = ['ip', ]

    list_display = ('ip', 'vlan', 'pos', 'func', 'assign', 'comment')


@admin.register(Pos)
class PosAdmin(admin.ModelAdmin):
    search_fields = ['name', ]

    list_display = ('name','desc')
