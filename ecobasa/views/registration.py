# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.decorators import method_decorator
from honeypot.decorators import check_honeypot
from userprofiles.views import RegistrationView

from ..forms import RegistrationMemberForm, RegistrationCommunityForm


class RegistrationView(RegistrationView):
    template_name = 'userprofiles/registration.html'
register = RegistrationView.as_view()


class RegistrationMemberView(RegistrationView):
    template_name = 'userprofiles/registration_member.html'
    form_class = RegistrationMemberForm

    @method_decorator(check_honeypot)
    def dispatch(self, request, *args, **kwargs):
        return super(RegistrationMemberView, self).dispatch(
            request, *args, **kwargs)

register_member = RegistrationMemberView.as_view()


class RegistrationCommunityView(RegistrationView):
    template_name = 'userprofiles/registration_community.html'
    form_class = RegistrationCommunityForm

    @method_decorator(check_honeypot)
    def dispatch(self, request, *args, **kwargs):
        return super(RegistrationCommunityView, self).dispatch(
            request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RegistrationCommunityView, self).get_context_data(**kwargs)
        context['formset_seed'] = self.form_class.SeedInlineFormSet(instance=None)
        return context

register_community = RegistrationCommunityView.as_view()
