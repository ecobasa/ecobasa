# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _
from userprofiles.forms import RegistrationForm

from cosinnus.forms.profile import UserProfileForm
from cosinnus.forms.widgets import DateL10nPicker
from cosinnus.models import (CosinnusGroup, CosinnusGroupMembership,
    MEMBERSHIP_ADMIN)

from .models import (EcobasaUserProfile, EcobasaCommunityProfile,
    EcobasaCommunityProfileSeed)


class RegistrationMemberForm(RegistrationForm):

    def __init__(self, *args, **kwargs):
        super(RegistrationMemberForm, self).__init__(*args, **kwargs)
        fields_user = forms.fields_for_model(EcobasaUserProfile)
        self.fields.update(fields_user)
        self.fields['birth_date'].widget = DateL10nPicker()

        # has_bus is a boolean field, but is represented as a button in the
        # form. Form validation has to be told explicitly that this field is
        # not required.
        self.fields['has_bus'] = forms.CharField(
            widget=forms.HiddenInput(),
            label=self.fields['has_bus'].label,
            required=False)

    def save_profile(self, new_user, *args, **kwargs):
        # do not catch DoesNotExist: there must be something else wrong
        profile = EcobasaUserProfile.objects.get(user=new_user)

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


class CommunityProfileForm(forms.ModelForm):
    SeedInlineFormSet = forms.models.inlineformset_factory(
        EcobasaCommunityProfile, EcobasaCommunityProfileSeed, extra=1)

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


class PioneerProfileForm(UserProfileForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
        'password_incorrect': _('Your old password was entered incorrectly. '
                                'Please enter it again.'),
    }
    old_password = forms.CharField(label=_('Old password'),
                                   required=False,
                                   widget=forms.PasswordInput)
    new_password1 = forms.CharField(label=_('New password'),
                                    required=False,
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=_('New password confirmation'),
                                    required=False,
                                    widget=forms.PasswordInput)
    email = forms.EmailField(label=_("Email"), max_length=254)

    def __init__(self, *args, **kwargs):
        super(PioneerProfileForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'].widget = DateL10nPicker()
        self.fields['email'].initial = self.instance.user.email

    def clean_old_password(self):
        """
        Validates that the old_password field is correct.
        """
        old_password = self.cleaned_data['old_password']
        if old_password and not self.instance.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'])
        return old_password

    def clean_new_password2(self):
        """
        Validates that the new password matches.
        """
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        user = self.instance.user
        user.email = self.cleaned_data['email']

        new_password = self.cleaned_data['new_password1']
        if new_password:
            user.set_password(new_password)

        if commit:
            user.save()
        return super(PioneerProfileForm, self).save(commit)
