# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import EcobasaCommunityProfile, EcobasaCommunityProfileSeed


class SeedAdmin(admin.TabularInline):
    model = EcobasaCommunityProfileSeed
    extra = 1

class EcobasaCommunityProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('contact_lat', 'contact_lon',)
    inlines = [SeedAdmin]

admin.site.register(EcobasaCommunityProfile, EcobasaCommunityProfileAdmin)
