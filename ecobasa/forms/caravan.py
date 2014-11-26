# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cosinnus.forms.tagged import get_form, TagObjectForm

from ..models import Caravan


# just subclassing CosinnusGroupForm doesn't work

class _CaravanForm(TagObjectForm):

    class Meta:
        fields = ('name', 'slug', 'description', 'public', 'offers', 'image')
        model = Caravan

    def __init__(self, *args, **kwargs):
        super(_CaravanForm, self).__init__(*args, **kwargs)
        self.fields['slug'].required = False


class CaravanForm(get_form(_CaravanForm, attachable=False)):
    pass
