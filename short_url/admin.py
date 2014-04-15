# -*- coding: utf-8 -*-

from django.contrib import admin

from short_url.models import ShortURLMap


class ShortURLMapAdmin(admin.ModelAdmin):
    list_display = ('short_url', 'short_url_link', 'long_url_link', 'created_on')
    search_fields = ['url', ]
    date_hierarchy = 'created_on'

admin.site.register(ShortURLMap, ShortURLMapAdmin)