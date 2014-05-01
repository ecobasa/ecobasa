# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, UpdateView, ListView
from cosinnus.models import CosinnusGroup
from cosinnus.models.group import MEMBERSHIP_ADMIN
from cosinnus.views.group import GroupListView
from cosinnus.views.user import UserListView, USER_MODEL
from cosinnus.views.profile import UserProfileUpdateView
from cosinnus.views.widget import DashboardMixin
from haystack.utils import Highlighter
from haystack.views import SearchView
from userprofiles.views import RegistrationView

from .forms import (CommunityProfileForm, PioneerProfileForm,
    RegistrationMemberForm, RegistrationCommunityForm)
from .models import OrganiserRole


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


class CommunityUpdateView(UpdateView):
    template_name = 'ecobasa/community_form.html'
    form_class = CommunityProfileForm

    def dispatch(self, *args, **kwargs):
        group = get_object_or_404(CosinnusGroup, slug=self.kwargs['group'])
        user = self.request.user
        if user.is_superuser or group.is_admin(user):
            self.group = group
            return super(CommunityUpdateView, self).dispatch(*args, **kwargs)
        else:
            raise PermissionDenied

    def get_object(self):
        return self.group.profile

    def get_context_data(self, **kwargs):
        context = super(CommunityUpdateView, self).get_context_data(**kwargs)
        context['formset_seed'] = self.form_class.SeedInlineFormSet(
            instance=self.object)
        return context

    def form_valid(self, form):
        result = super(CommunityUpdateView, self).form_valid(form)
        messages.success(self.request,
            _('The profile was successfully updated.'))
        return result

    def get_success_url(self):
        kwargs = {'group': self.group.slug}
        return reverse('community-detail', kwargs=kwargs)

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

    def get_context_data(self, *args, **kwargs):
        context = super(PioneerDetailView, self).get_context_data(
            *args, **kwargs)
        context['object'].organiser_roles = OrganiserRole.objects.for_user(
            context['object'])
        return context

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


#############################################################################
# find views
#############################################################################

class FindView(SearchView):
    def get_results(self):
        """
        Override get_results to add the value of the field where query was found
        Also takes care of highlighting the query.
        """
        results = super(FindView, self).get_results()
        query = self.query.lower()
        highlight = Highlighter(query)
        for r in results:
            for field in r.get_stored_fields():
                value = getattr(r, field)
                # assume search index field 'text' is document field
                if query in value.lower() and field != 'text':
                    # assume search index field name == model field name
                    try:
                        name = r.object._meta.get_field(field).verbose_name
                    except:
                        name = field
                    r.context = {
                        'field': name,
                        'value': highlight.highlight(value)
                    }
                    continue
        return results

# SearchView is no Django view, so no "find = FindView.as_view()"


#############################################################################
# organiser views
#############################################################################


class OrganiserListView(ListView):
    model = OrganiserRole
    template_name = 'ecobasa/organiser_list.html'

organiser_list = OrganiserListView.as_view()
