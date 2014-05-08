# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from ..models import EcobasaUserProfile
register = template.Library()


@register.assignment_tag
def get_buses():
    return EcobasaUserProfile.objects.has_bus
