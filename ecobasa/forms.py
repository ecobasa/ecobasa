# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from userprofiles.forms import RegistrationForm

from .models import EcobasaUserProfile


class EcobasaRegistrationForm(RegistrationForm):
    myfield = forms.CharField(label=_('myfield'), required=True)

    def save_profile(self, new_user, *args, **kwargs):
        # do not catch DoesNotExist: there must be something else wrong
        profile = EcobasaUserProfile.objects.get(user=new_user)
        profile.myfield = self.cleaned_data['myfield']
        profile.save()
