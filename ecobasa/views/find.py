# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from haystack.utils import Highlighter
from haystack.views import SearchView
from six import string_types


class FindView(SearchView):
    def get_results(self):
        """
        Override get_results to add the value of the field where query was found
        Also takes care of highlighting the query.
        """
        results = super(FindView, self).get_results()
        query = self.query.lower()
        highlight = Highlighter(query)
        for r in results:
            for field in r.get_stored_fields():
                value = getattr(r, field)
                # assume search index field 'text' is document field
                if isinstance(value, string_types) and\
                        query in value.lower() and\
                        field != 'text':
                    # assume search index field name == model field name
                    try:
                        name = r.object._meta.get_field(field).verbose_name
                    except:
                        name = field
                    r.context = {
                        'field': name,
                        'value': highlight.highlight(value)
                    }
                    continue
        return results

# SearchView is no Django view, so no "find = FindView.as_view()"
