# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
import json

from ..models.caravan import TaggedOffers

register = template.Library()


@register.assignment_tag
def get_offers():
    qs = TaggedOffers.objects.all().select_related('tag')
    names = set(map(lambda x: x.tag.name, qs))
    return json.dumps(list(names))
