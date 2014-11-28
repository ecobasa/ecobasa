# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

register = template.Library()


@register.filter
def all_day(event):
    duration = event.to_date - event.from_date
    if duration.days < 1:
        return 'false'
    else:
        return 'true'
