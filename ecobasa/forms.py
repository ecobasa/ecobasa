# -*- coding: utf-8 -*-

from django import forms
from userprofiles.forms import RegistrationForm

from cosinnus.forms.widgets import DateL10nPicker
from .models import EcobasaUserProfile


class EcobasaRegistrationForm(RegistrationForm):
    model_fields = forms.fields_for_model(EcobasaUserProfile)

    def __init__(self, *args, **kwargs):
        super(EcobasaRegistrationForm, self).__init__(*args, **kwargs)
        self.fields.update(self.model_fields)
        self.fields['birth_date'].widget = DateL10nPicker()

    def save_profile(self, new_user, *args, **kwargs):
        # do not catch DoesNotExist: there must be something else wrong
        profile = EcobasaUserProfile.objects.get(user=new_user)

        profile.avatar = self.cleaned_data['avatar']
        profile.gender = self.cleaned_data['gender']
        profile.birth_date = self.cleaned_data['birth_date']
        profile.country = self.cleaned_data['country']
        profile.city = self.cleaned_data['city']
        profile.zipcode = self.cleaned_data['zipcode']

        profile.has_bus = self.cleaned_data['has_bus']
        profile.bus_consumption = self.cleaned_data['bus_consumption']
        profile.bus_has_driving_license =\
            self.cleaned_data['bus_has_driving_license']
        profile.bus_image = self.cleaned_data['bus_image']
        profile.bus_num_passengers = self.cleaned_data['bus_num_passengers']
        profile.bus_others_can_drive =\
            self.cleaned_data['bus_others_can_drive']

        for tag in self.cleaned_data['interests']:
            profile.interests.add(tag)
        for tag in self.cleaned_data['skills']:
            profile.skills.add(tag)
        for tag in self.cleaned_data['products']:
            profile.products.add(tag)

        profile.save()
