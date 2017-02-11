from django.contrib import admin
from shortcut.models import Shortcut


@admin.register(Shortcut)
class ShortcutAdmin(admin.ModelAdmin):
    search_fields = ['name', 'user', ]
    list_display = ['user', 'name', 'website', 'show', 'add_date', 'comment']
