# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from ..models import OrganiserRole

register = template.Library()


@register.assignment_tag
def get_organiser_roles_for_user(user):
    """
    Group a user's organiser roles by group.
    See ecobasa/templates/ecobasa/pioneer_detail.html for usage.
    """
    roles = OrganiserRole.objects.for_user(user)
    grouped = {}
    for role in roles:
        group_name = role.cosinnus_group_membership.group.name
        if group_name not in grouped:
            grouped[group_name] = []
        grouped[group_name].append(role)
    return grouped


@register.assignment_tag
def get_organiser_roles():
    """
    Group all organiser roles by user.
    See ecobasa/templates/ecobasa/includes/organisers.html for usage.
    """
    roles = OrganiserRole.objects.all()
    grouped = {}
    for role in roles:
        username = role.cosinnus_group_membership.user.username
        if username not in grouped:
            grouped[username] = []
        grouped[username].append(role)
    return grouped
