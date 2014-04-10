# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from haystack.indexes import BasicSearchIndex, Indexable

from .models import EcobasaCommunityProfile


class EcobasaCommunityProfileIndex(BasicSearchIndex, Indexable):
    address_fields = ['contact_telephone', 'contact_street',
        'contact_zipcode', 'contact_city', 'contact_country']

    def get_model(self):
        return EcobasaCommunityProfile

    def index_queryset(self, using=None):
        "Used when the entire index for model is updated."
        return EcobasaCommunityProfile.objects.all()

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
