# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from ..models import EcobasaCommunityProfile, EcobasaCommunityProfileSeed


class CommunityProfileForm(forms.ModelForm):
    SeedInlineFormSet = forms.models.inlineformset_factory(
        EcobasaCommunityProfile, EcobasaCommunityProfileSeed, extra=1)
    contact_location_lat = forms.CharField(widget=forms.HiddenInput())
    contact_location_lon = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = EcobasaCommunityProfile

    def save(self, commit=True):
        formset = self.SeedInlineFormSet(self.data, instance=self.instance)
        for form in formset:
            if form.is_valid():
                # is_valid populates cleaned_data
                data = form.cleaned_data
                if data and data['kind'] and data['num']:
                    if data['DELETE']:
                        data['id'].delete()
                    else:
                        form.save(commit)
        return super(CommunityProfileForm, self).save(commit)
