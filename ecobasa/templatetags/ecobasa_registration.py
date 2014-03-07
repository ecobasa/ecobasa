# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from ..models import (TaggedInterest, TaggedSkill, TaggedProduct,
    TaggedOffersService, TaggedOffersSkill, TaggedOffersCreation)

register = template.Library()


def get_tagnames(model):
    qs = model.objects.all().select_related('tag')
    return set(map(lambda x: x.tag.name, qs))


@register.assignment_tag
def get_interests():
    return get_tagnames(TaggedInterest)


@register.assignment_tag
def get_skills():
    return get_tagnames(TaggedSkill)


@register.assignment_tag
def get_products():
    return get_tagnames(TaggedProduct)


@register.assignment_tag
def get_offers_services():
    return get_tagnames(TaggedOffersService)


@register.assignment_tag
def get_offers_skills():
    return get_tagnames(TaggedOffersSkill)


@register.assignment_tag
def get_offers_creations():
    return get_tagnames(TaggedOffersCreation)
