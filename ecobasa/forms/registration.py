# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from userprofiles.forms import RegistrationForm

from cosinnus.forms.widgets import DateL10nPicker
from cosinnus.models import (CosinnusGroup, CosinnusGroupMembership,
    MEMBERSHIP_ADMIN)

from ..models import (EcobasaUserProfile, EcobasaCommunityProfile,
    EcobasaCommunityProfileSeed)


class RegistrationMemberForm(RegistrationForm):

    def __init__(self, *args, **kwargs):
        super(RegistrationMemberForm, self).__init__(*args, **kwargs)
        fields_user = forms.fields_for_model(EcobasaUserProfile)
        self.fields.update(fields_user)
        self.fields['birth_date'].widget = DateL10nPicker()
        self.fields['avatar'].required = True

        # has_bus is a boolean field, but is represented as a button in the
        # form. Form validation has to be told explicitly that this field is
        # not required.
        self.fields['has_bus'] = forms.CharField(
            widget=forms.HiddenInput(),
            label=self.fields['has_bus'].label,
            required=False)

    def save_profile(self, new_user, *args, **kwargs):
        # cosinnus should have created the profile already, but do _or_create
        # just in case
        profile, _ = EcobasaUserProfile.objects.get_or_create(user=new_user)

        profile.avatar = self.cleaned_data['avatar']
        profile.gender = self.cleaned_data['gender']
        profile.birth_date = self.cleaned_data['birth_date']
        profile.country = self.cleaned_data['country']
        profile.city = self.cleaned_data['city']
        profile.zipcode = self.cleaned_data['zipcode']

        profile.ecobasa_member = self.cleaned_data['ecobasa_member']

        profile.tour_why = self.cleaned_data['tour_why']
        profile.tour_how = self.cleaned_data['tour_how']

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


class RegistrationCommunityForm(RegistrationForm):
    SeedInlineFormSet = forms.models.inlineformset_factory(
        EcobasaCommunityProfile, EcobasaCommunityProfileSeed, extra=1)

    def __init__(self, *args, **kwargs):
        super(RegistrationCommunityForm, self).__init__(*args, **kwargs)
        fields_user = forms.fields_for_model(EcobasaUserProfile)
        self.fields.update(fields_user)
        self.fields['birth_date'].widget = DateL10nPicker()

        fields_community = forms.fields_for_model(EcobasaCommunityProfile)
        fields_community['contact_location_lat'].widget = forms.HiddenInput()
        fields_community['contact_location_lon'].widget = forms.HiddenInput()
        self.fields.update(fields_community)

    def save_profile(self, new_user, *args, **kwargs):
        name = self.cleaned_data['name']

        # set up cosinnus group and admin user
        community = CosinnusGroup.objects.create(name=name, public=False)
        CosinnusGroupMembership.objects.create(
            user=new_user, group=community, status=MEMBERSHIP_ADMIN)

        # set up profile
        profile = EcobasaCommunityProfile.objects.create(group=community)
        profile.name = name
        profile.contact_telephone = self.cleaned_data['contact_telephone']
        profile.contact_street = self.cleaned_data['contact_street']
        profile.contact_location = self.cleaned_data['contact_location']
        profile.contact_location_lat = self.cleaned_data['contact_location_lat']
        profile.contact_location_lon = self.cleaned_data['contact_location_lon']
        profile.contact_city = self.cleaned_data['contact_city']
        profile.contact_zipcode = self.cleaned_data['contact_zipcode']
        profile.contact_country = self.cleaned_data['contact_country']
        profile.contact_show = self.cleaned_data['contact_show']

        profile.visitors_num = self.cleaned_data['visitors_num']
        profile.visitors_accommodation =\
            self.cleaned_data['visitors_accommodation']

        profile.wishlist_materials = self.cleaned_data['wishlist_materials']
        profile.wishlist_tools = self.cleaned_data['wishlist_tools']
        profile.wishlist_special_needs =\
            self.cleaned_data['wishlist_special_needs']

        for tag in self.cleaned_data['offers_services']:
            profile.offers_services.add(tag)
        for tag in self.cleaned_data['offers_skills']:
            profile.offers_skills.add(tag)
        for tag in self.cleaned_data['offers_creations']:
            profile.offers_creations.add(tag)
        profile.offers_workshop_spaces =\
            self.cleaned_data['offers_workshop_spaces']
        profile.offers_learning_seminars =\
            self.cleaned_data['offers_learning_seminars']

        profile.basic_inhabitants = self.cleaned_data['basic_inhabitants']
        profile.basic_inhabitants_underage =\
            self.cleaned_data['basic_inhabitants_underage']
        profile.basic_brings_together =\
            self.cleaned_data['basic_brings_together']
        profile.basic_membership_status =\
            self.cleaned_data['basic_membership_status']

        profile.save()

        # seed stuff
        formsets = self.SeedInlineFormSet(self.data, instance=profile)
        for formset in formsets:
            if formset.is_valid():
                formset.save()
