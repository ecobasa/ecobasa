# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
import json

from ..models import (TaggedInterest, TaggedSkill, TaggedProduct, TaggedOffersService, TaggedOffersSkill, TaggedOffersCreation, TaggedOffersMaterial, TaggedOffersTool, TaggedWishSkill, TaggedWishMaterial, TaggedWishTool, TaggedReferenceProduct, TaggedReferenceService, TaggedReferenceSkill)

register = template.Library()


def get_tagnames(model):
    qs = model.objects.all().select_related('tag')
    names = set(map(lambda x: x.tag.name, qs))
    return json.dumps(list(names))


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

@register.assignment_tag
def get_offers_materials():
    return get_tagnames(TaggedOffersMaterial)

@register.assignment_tag
def get_offers_tools():
    return get_tagnames(TaggedOffersTool)

@register.assignment_tag
def get_wishlist_skills():
    return get_tagnames(TaggedWishSkill)

@register.assignment_tag
def get_wishlist_materials():
    return get_tagnames(TaggedWishMaterial)

@register.assignment_tag
def get_wishlist_tools():
    return get_tagnames(TaggedWishTool)


@register.assignment_tag
def get_reference_products():
    return get_tagnames(TaggedReferenceProduct)


@register.assignment_tag
def get_reference_services():
    return get_tagnames(TaggedReferenceService)


@register.assignment_tag
def get_reference_skills():
    return get_tagnames(TaggedReferenceSkill)
