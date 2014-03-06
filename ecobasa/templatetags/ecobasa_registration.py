# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from ..models import (TaggedInterest, TaggedSkill, TaggedProduct,
    TaggedOffersService, TaggedOffersSkill, TaggedOffersCreation)

register = template.Library()


def map_tagmodel(model):
    return map(lambda x: x.tag.name, model.objects.all())


@register.assignment_tag
def get_interests():
    return map_tagmodel(TaggedInterest)


@register.assignment_tag
def get_skills():
    return map_tagmodel(TaggedSkill)


@register.assignment_tag
def get_products():
    return map_tagmodel(TaggedProduct)


@register.assignment_tag
def get_offers_services():
    return map_tagmodel(TaggedOffersService)


@register.assignment_tag
def get_offers_skills():
    return map_tagmodel(TaggedOffersSkill)


@register.assignment_tag
def get_offers_creations():
    return map_tagmodel(TaggedOffersCreation)
