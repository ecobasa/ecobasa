# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, UpdateView, ListView


from cosinnus.models import CosinnusGroup
from cosinnus.models.group import MEMBERSHIP_ADMIN, MEMBERSHIP_PENDING
from cosinnus.views.group import GroupListView
from cosinnus.views.widget import DashboardMixin
from cosinnus_note.models import Note

from ..forms import CommunityProfileForm
from ..models import Reference
from .reference import ReferenceAddView, ReferenceEditView, get_tag_counts


class CommunityDetailView(DetailView):
    MAX_REFERENCES = 10
    model = CosinnusGroup
    slug_url_kwarg = 'group'
    template_name = 'ecobasa/community_detail.html'

    def _can_add_reference(self):
        if not self.request.user.is_authenticated():
            return False
        qs = Reference.objects.filter(
            giver=self.request.user, receiver_community=self.object)
        return len(qs) == 0

    def get_context_data(self, **kwargs):
        context = super(CommunityDetailView, self).get_context_data(**kwargs)
        context['profile'] = self.object.profile

        # CosinnusGroup.admins and .pendings return pks, not objects :(
        # So does CosinnusGroupMembership.get_pendings/admins :((
        context['object'].ambassadors = map(lambda x: x.user,
            context['object'].memberships.filter(status=MEMBERSHIP_ADMIN))
        context['object'].pending_members = map(lambda x: x.user,
            context['object'].memberships.filter(status=MEMBERSHIP_PENDING))
        context['posts'] = Note.objects.filter(group=context['object'])

        references = self.object.ecobasa_reference_receiver_community.all();
        context['references'] = {
            'tag_counts': get_tag_counts(references),
            'references': references[:self.MAX_REFERENCES],
        }
        context['can_add_reference'] = self._can_add_reference()

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


class CommunityReferenceAddView(ReferenceAddView):
    template_name = 'ecobasa/community_reference_form.html'

    def get_form(self, form_class):
        self.receiver['pioneer'] = None
        self.receiver['community'] = get_object_or_404(
            CosinnusGroup, slug=self.kwargs['group'])
        return super(CommunityReferenceAddView, self).get_form(form_class)

    def get_context_data(self, *args, **kwargs):
        context = super(CommunityReferenceAddView, self).get_context_data(
            *args, **kwargs)
        context['community'] = self.receiver['community']
        context['page_title'] = _('Add reference for %(community)s') % {
            'community': self.receiver['community'].name,
        }
        context['page_h1'] = _('Add reference')
        context['form_action'] = _('Add')
        return context

    def form_valid(self, form):
        result = super(CommunityReferenceAddView, self).form_valid(form)
        messages.success(self.request,
            _('The reference was successfully added.'))
        return result

    def get_success_url(self):
        return reverse('community-detail', kwargs={
            'group': self.object.receiver_community.slug
        })

community_reference_add = CommunityReferenceAddView.as_view()


class CommunityReferenceEditView(ReferenceEditView):
    template_name = 'ecobasa/community_reference_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CommunityReferenceEditView, self).get_context_data(
            *args, **kwargs)
        context['community'] = self.object.receiver_community
        context['page_title'] = _('Edit reference for %(community)s') % {
            'community': self.object.receiver_community.name,
        }
        context['page_h1'] = _('Edit reference')
        context['form_action'] = _('Edit')
        return context

    def form_valid(self, form):
        result = super(CommunityReferenceEditView, self).form_valid(form)
        messages.success(self.request,
            _('The reference was successfully edited.'))
        return result

    def get_success_url(self):
        return reverse('community-detail', kwargs={
            'group': self.object.receiver_community.slug
        })

community_reference_edit = CommunityReferenceEditView.as_view()


class CommunityReferenceListView(ListView):
    template_name = 'ecobasa/community_reference_list.html'
    model = Reference

    def get(self, request, *args, **kwargs):
        self.community = get_object_or_404(
            CosinnusGroup, slug=self.kwargs['group'])
        return super(CommunityReferenceListView, self).get(
            request, *args, **kwargs)

    def get_queryset(self):
        qs = super(CommunityReferenceListView, self).get_queryset()
        return qs.filter(receiver_community=self.community)

    def get_context_data(self, *args, **kwargs):
        context = super(CommunityReferenceListView, self).get_context_data(
            *args, **kwargs)
        context['community'] = self.community
        return context

community_reference_list = CommunityReferenceListView.as_view()
