# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from ..models import EcobasaCommunityProfile
register = template.Library()


@register.assignment_tag
def get_community_locations():
    def mkloc(community):
        return {
            'lat': community.contact_lat,
            'lon': community.contact_lon,
            'name': community.name,
            'slug': community.group.slug,
        }

    qs = EcobasaCommunityProfile.objects.all().select_related('group')
    locations = [mkloc(c) for c in qs if c.contact_lat and c.contact_lon]
    return locations
