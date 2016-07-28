# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from ..models import Reference


class ReferenceForm(forms.ModelForm):

    class Meta:
        model = Reference
        widgets = {
            'recommend': forms.RadioSelect
        }

    def __init__(self, *args, **kwargs):
        super(ReferenceForm, self).__init__(*args, **kwargs)
        self.fields['giver'].widget = forms.HiddenInput()
        self.fields['receiver_pioneer'].widget = forms.HiddenInput()
        self.fields['receiver_community'].widget = forms.HiddenInput()


def get_form(request, receiver):
    user = request.user

    # no form if not authenticated
    if not user.is_authenticated():
        return None

    # no form if receiver is same as user
    if user == receiver['pioneer']:
        return None

    # no form if user has given already
    if Reference.objects.filter(
            giver=user,
            receiver_pioneer=receiver['pioneer'],
            receiver_community=receiver['community']):
        return None

    if request.method == 'POST':
        return ReferenceForm(request.POST)
    else:
        initial = {
            'giver': user,
            'receiver_pioneer': receiver['pioneer'],
            'receiver_community': receiver['community'],
        }
        return ReferenceForm(initial=initial)
