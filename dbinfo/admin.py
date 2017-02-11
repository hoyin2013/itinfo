from django.contrib import admin
from dbinfo.models import Dbserver, Users, Mysqluser, Sysusers


@admin.register(Dbserver)
class DbserverAdmin(admin.ModelAdmin):
    search_fields = ['name', 'ip', 'pos']

    list_display = ('name', 'ip', 'pos', 'firm', 'model', 'feature', 'buy_time', 'service_range', 'comment')


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    search_fields = ['user', 'status']

    list_display = ['dbserver','user', 'passwd', 'tablespace', 'status', 'business', 'created', 'comment']


@admin.register(Mysqluser)
class MysqluserAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('dbserver', 'name', 'passwd', 'dbname', 'business', 'comment')


@admin.register(Sysusers)
class SysusersAdmin(admin.ModelAdmin):
    list_display = ('dbserver', 'name', 'user', 'passwd')
