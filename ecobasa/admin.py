# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import (EcobasaCommunityProfile, EcobasaCommunityProfileSeed,
                     OrganiserRole, Caravan)


class SeedAdmin(admin.TabularInline):
    model = EcobasaCommunityProfileSeed
    extra = 1


class EcobasaCommunityProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('contact_lat', 'contact_lon',)
    inlines = [SeedAdmin]

admin.site.register(EcobasaCommunityProfile, EcobasaCommunityProfileAdmin)


class OrganiserRoleAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('__unicode__', 'title', 'get_user', 'get_group',)
    list_filter = ('cosinnus_group_membership__group',)

    def get_user(self, obj):
        return obj.cosinnus_group_membership.user
    get_user.short_description = _('User')

    def get_group(self, obj):
        return obj.cosinnus_group_membership.group
    get_group.short_description = _('Group')

admin.site.register(OrganiserRole, OrganiserRoleAdmin)


class CaravanAdmin(admin.ModelAdmin):
    pass
admin.site.register(Caravan, CaravanAdmin)
