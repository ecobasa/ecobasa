# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.conf import settings

from cosinnus.models import CosinnusGroup
from cosinnus_note.models import Note
from ..models import EcobasaCommunityProfile

from django.contrib.auth import get_user_model
from ..models import EcobasaUserProfile

register = template.Library()


@register.assignment_tag
def get_community_locations():
    def mkloc(com):
        return {
            'lat': com.contact_location_lat,
            'lon': com.contact_location_lon,
            'name': com.name,
            'slug': com.group.slug,
            'image': com.image,
            'text': com.basic_description,
            'text2': com.basic_brings_together,
            'members': com.basic_inhabitants,
            'visitors': com.visitors_num,
            'status': com.basic_membership_status,
            'type': com.community_type,
            'status': com.community_status,
        }

    qs = EcobasaCommunityProfile.objects.all().select_related('group')
    locations = [mkloc(c)
        for c in qs if c.contact_location_lat and c.contact_location_lon]
    return locations

@register.assignment_tag
def get_pioneer_locations():
    def mkloc(pioneer):
        return {
            'lat': pioneer.address_lat,
            'lon': pioneer.address_lon,
            'name': pioneer.user,
            'image': pioneer.avatar,
            'text': pioneer.about,
            'text2': pioneer.world,
            'skills': pioneer.skills.all,
        }

    qs = EcobasaUserProfile.objects.all().select_related('user')
    locations = [mkloc(p)
        for p in qs if p.address_lat and p.address_lon]
    return locations


@register.inclusion_tag('ecobasa/start_blog.html', takes_context=True)
def show_blog_posts(context):
    pk = getattr(settings, 'ECOBASA_GROUP', 1)
    try:
        group = CosinnusGroup.objects.filter(pk=pk)[0]
    except IndexError:
        posts = []
    else:
        posts = Note.objects.filter(
            group=group, media_tag__public=True)[0:3]

    context['posts'] = posts
    return context

@register.inclusion_tag('ecobasa/announcements.html', takes_context=True)
def show_announcements(context):
    pk = getattr(settings, 'ECOBASA_SPECIAL_COSINNUS_GROUP', 1)
    try:
        group = CosinnusGroup.objects.filter(pk=pk)[0]
    except IndexError:
        announcements = []
    else:
        announcements = Note.objects.filter(
            group=group, media_tag__public=True)

    context['announcements'] = announcements
    return context