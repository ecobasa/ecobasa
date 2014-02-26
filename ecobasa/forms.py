# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from userprofiles.forms import RegistrationForm

from .models import EcobasaUserProfile


class EcobasaRegistrationForm(RegistrationForm):
    model_fields = forms.fields_for_model(EcobasaUserProfile)

    def __init__(self, *args, **kwargs):
        super(EcobasaRegistrationForm, self).__init__(*args, **kwargs)
        self.fields.update(self.model_fields)

    def save_profile(self, new_user, *args, **kwargs):
        # do not catch DoesNotExist: there must be something else wrong
        profile = EcobasaUserProfile.objects.get(user=new_user)
        for field in self.model_fields.keys():
            setattr(profile, field, self.cleaned_data[field])
        profile.save()
