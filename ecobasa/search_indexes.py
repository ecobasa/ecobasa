# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import six
from haystack.fields import CharField, SearchField
from haystack.indexes import BasicSearchIndex, Indexable

from .models import EcobasaCommunityProfile, EcobasaUserProfile


class TaggableField(SearchField):
    field_type = 'taggable'

    def prepare(self, obj):
        taggable_manager = getattr(obj, self.model_attr)
        strings = [six.text_type(x) for x in taggable_manager.all()]
        return ', '.join(strings)


class EcobasaCommunityProfileIndex(BasicSearchIndex, Indexable):
    address_fields = ['contact_telephone', 'contact_street',
        'contact_zipcode', 'contact_city', 'contact_country']
    name = CharField(model_attr='name')
    slug = CharField(model_attr='group__slug')
    contact_telephone = CharField(model_attr='contact_telephone', null=True)
    contact_street = CharField(model_attr='contact_street', null=True)
    contact_zipcode = CharField(model_attr='contact_zipcode', null=True)
    contact_city = CharField(model_attr='contact_city', null=True)
    contact_country = CharField(model_attr='contact_country', null=True)
    visitors_accommodation = CharField(model_attr='visitors_accommodation', null=True)
    wishlist_materials = CharField(model_attr='wishlist_materials', null=True)
    wishlist_tools = CharField(model_attr='wishlist_tools', null=True)
    wishlist_special_needs = CharField(model_attr='wishlist_special_needs', null=True)
    offers_creations = TaggableField(model_attr='offers_creations', null=True)
    offers_services = TaggableField(model_attr='offers_services', null=True)
    offers_skills = TaggableField(model_attr='offers_skills', null=True)
    offers_learning_seminars = CharField(model_attr='offers_learning_seminars', null=True)
    offers_workshop_spaces = CharField(model_attr='offers_workshop_spaces', null=True)
    basic_brings_together = CharField(model_attr='basic_brings_together', null=True)

    def get_model(self):
        return EcobasaCommunityProfile

    def prepare_text(self, obj):
        """FIXME: can this be done using the API properly?
        The problem is that we can't filter the object if contact_show is False.
        We want it to appear if searched by e.g. name, but we don't want it to
        appear if searched by one of the address fields.
        This solution removes the object's address fields from the
        search index's document (text) field.
        """
        text = self.prepared_data['text']

        if not obj.contact_show:
            for field in self.address_fields:
                value = getattr(obj, field)
                if value:
                    text = text.replace(value, '')

        return text


class EcobasaUserProfileIndex(BasicSearchIndex, Indexable):
    username = CharField(model_attr='user__username')
    interests = TaggableField(model_attr='interests')
    products = TaggableField(model_attr='products')
    skills = TaggableField(model_attr='skills')

    def get_model(self):
        return EcobasaUserProfile
