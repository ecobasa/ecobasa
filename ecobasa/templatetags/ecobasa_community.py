# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from ..models import EcobasaCommunityProfile
register = template.Library()


@register.assignment_tag
def get_community_locations():
    qs = EcobasaCommunityProfile.objects.all()
    return [{
        'lat': c.contact_lat, 'lon': c.contact_lon, 'name': c.name, 'slug': c.group.slug
    } for c in qs]

