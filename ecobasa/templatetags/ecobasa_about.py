# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django import template

register = template.Library()


@register.filter
def to_datetime(value):
    return datetime.strptime(value, '%Y-%m-%d')
