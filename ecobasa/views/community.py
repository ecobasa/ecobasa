# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, UpdateView

from cosinnus.models import CosinnusGroup
from cosinnus.models.group import MEMBERSHIP_ADMIN, MEMBERSHIP_PENDING
from cosinnus.views.group import GroupListView
from cosinnus.views.widget import DashboardMixin

from ..forms import CommunityProfileForm


class CommunityDetailView(DetailView):
    model = CosinnusGroup
    slug_url_kwarg = 'group'
    template_name = 'ecobasa/community_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CommunityDetailView, self).get_context_data(**kwargs)
        context['profile'] = self.object.profile

        # CosinnusGroup.admins and .pendings return pks, not objects :(
        # So does CosinnusGroupMembership.get_pendings/admins :((
        context['object'].ambassadors = map(lambda x: x.user,
            context['object'].memberships.filter(status=MEMBERSHIP_ADMIN))
        context['object'].pending_members = map(lambda x: x.user,
            context['object'].memberships.filter(status=MEMBERSHIP_PENDING))

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
        # a community is a group with a profile
        return self.model.objects.filter(profile__isnull=False)

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
