# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from ..models import TaggedInterest, TaggedSkill, TaggedProduct

register = template.Library()


@register.assignment_tag
def get_interests():
    return map(lambda x: x.tag.name, TaggedInterest.objects.all())


@register.assignment_tag
def get_skills():
    return map(lambda x: x.tag.name, TaggedSkill.objects.all())


@register.assignment_tag
def get_products():
    return map(lambda x: x.tag.name, TaggedProduct.objects.all())
