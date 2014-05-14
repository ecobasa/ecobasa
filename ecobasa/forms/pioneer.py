# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from cosinnus.forms.profile import UserProfileForm
from cosinnus.forms.widgets import DateL10nPicker


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
