# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from ..models import EcobasaCommunityProfile
register = template.Library()


@register.assignment_tag
def get_community_locations():
    def mkloc(com):
        return {
            'lat': com.contact_location_lat,
            'lon': com.contact_location_lon,
            'name': com.name,
            'slug': com.group.slug,
        }

    qs = EcobasaCommunityProfile.objects.all().select_related('group')
    locations = [mkloc(c)
        for c in qs if c.contact_location_lat and c.contact_location_lon]
    return locations
