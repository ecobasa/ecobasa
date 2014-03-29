# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import EcobasaCommunityProfile


class EcobasaCommunityProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('contact_lat', 'contact_lon',)

admin.site.register(EcobasaCommunityProfile, EcobasaCommunityProfileAdmin)
