# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, UpdateView
from cosinnus.models import CosinnusGroup
from cosinnus.models.group import MEMBERSHIP_ADMIN
from cosinnus.views.group import GroupListView, GroupUpdateView
from cosinnus.views.user import UserListView, USER_MODEL
from cosinnus.views.profile import UserProfileUpdateView
from cosinnus.views.widget import DashboardMixin
from userprofiles.views import RegistrationView

from .forms import (PioneerProfileForm,
    RegistrationMemberForm, RegistrationCommunityForm)


class CommunityDetailView(DetailView):
    model = CosinnusGroup
    slug_url_kwarg = 'group'
    template_name = 'ecobasa/community_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CommunityDetailView, self).get_context_data(**kwargs)
        context['profile'] = self.object.profile
        return context

community_detail = CommunityDetailView.as_view()


class CommunityDashboardView(DashboardMixin, DetailView):
    """Not really useful yet."""
    model = CosinnusGroup
    slug_url_kwarg = 'group'
    context_object_name = 'group'

    def get_filter(self):
        return {'group_id': self.object.pk}

community_dashboard = CommunityDashboardView.as_view()


class CommunityListView(GroupListView):
    template_name = 'ecobasa/community_list.html'

    def get_queryset(self):
        return self.model.objects.all()

community_list = CommunityListView.as_view()


class CommunityUpdateView(GroupUpdateView):
    template_name = 'ecobasa/community_form.html'

community_update = CommunityUpdateView.as_view()


class PioneerListView(UserListView):
    template_name = 'ecobasa/pioneer_list.html'

    def get_queryset(self):
       users = super(PioneerListView, self).get_queryset()
       pioneers = users.exclude(cosinnus_memberships__status=MEMBERSHIP_ADMIN)
       pioneers = pioneers.exclude(is_superuser=True, is_staff=True)
       return pioneers

pioneer_list = PioneerListView.as_view()


class PioneerDetailView(DetailView):
    """
    cosinnus has a weird requirement to require staff to see a user's details.
    """
    model = USER_MODEL
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'ecobasa/pioneer_detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PioneerDetailView, self).dispatch(*args, **kwargs)


pioneer_detail = PioneerDetailView.as_view()


class PioneerUpdateView(UpdateView):
    """
    Alas, cosinnus' UserUpdateView only allows to edit the logged-in user's
    profile.
    """
    form_class = PioneerProfileForm
    template_name = 'ecobasa/pioneer_form.html'

    def get_object(self):
        user = get_object_or_404(USER_MODEL, username=self.kwargs['username'])
        return user.cosinnus_profile

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if user.is_superuser or user.username == self.kwargs['username']:
            return super(PioneerUpdateView, self).dispatch(*args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
        result = super(PioneerUpdateView, self).form_valid(form)
        messages.success(self.request,
            _('The profile was successfully updated.'))
        return result

    def get_success_url(self):
        kwargs = {'username': self.object.user.username}
        return reverse('pioneer-detail', kwargs=kwargs)

pioneer_update = PioneerUpdateView.as_view()



class BusListView(UserListView):
    template_name = 'ecobasa/bus_list.html'

    def get_context_data(self, **kwargs):
        context = super(BusListView, self).get_context_data(**kwargs)
        #import pdb; pdb.set_trace()
        context['user_list'] = context['user_list'].filter(cosinnus_profile__has_bus=True)
        #context['user_list'] = [user.name for user in context['user_list'] if user.has_bus == True]
        return context

bus_list = BusListView.as_view()


class BusAddView(UserProfileUpdateView):
    template_name = 'ecobasa/bus_add.html'

    def get_success_url(self):
        return reverse('bus-list')

bus_add = BusAddView.as_view()


#############################################################################
# registration overrides
#############################################################################

class RegistrationView(RegistrationView):
    template_name = 'userprofiles/registration.html'
register = RegistrationView.as_view()


class RegistrationMemberView(RegistrationView):
    template_name = 'userprofiles/registration_member.html'
    form_class = RegistrationMemberForm
register_member = RegistrationMemberView.as_view()


class RegistrationCommunityView(RegistrationView):
    template_name = 'userprofiles/registration_community.html'
    form_class = RegistrationCommunityForm

    def get_context_data(self, **kwargs):
        context = super(RegistrationCommunityView, self).get_context_data(**kwargs)
        context['formset_seed'] = self.form_class.SeedInlineFormSet(instance=None)
        return context

register_community = RegistrationCommunityView.as_view()
