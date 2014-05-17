# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, UpdateView, ListView

from cosinnus.models.group import MEMBERSHIP_ADMIN
from cosinnus.views.user import UserListView, USER_MODEL

from ..forms import PioneerProfileForm
from ..models import Reference
from .reference import ReferenceAddView, ReferenceEditView, get_tag_counts


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
    MAX_REFERENCES = 10
    model = USER_MODEL
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'ecobasa/pioneer_detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PioneerDetailView, self).dispatch(*args, **kwargs)

    def _can_add_reference(self):
        qs = Reference.objects.filter(
            giver=self.request.user, receiver_pioneer=self.object)
        return len(qs) == 0

    def get_context_data(self, **kwargs):
        context = super(PioneerDetailView, self).get_context_data(**kwargs)

        references = self.object.ecobasa_reference_receiver_pioneer.all();
        context['references'] = {
            'tag_counts': get_tag_counts(references),
            'references': references[:self.MAX_REFERENCES],
        }
        context['can_add_reference'] = self._can_add_reference()

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


class PioneerReferenceAddView(ReferenceAddView):
    template_name = 'ecobasa/pioneer_reference_form.html'

    def get_form(self, form_class):
        self.receiver['pioneer'] = get_object_or_404(
            get_user_model(), username=self.kwargs['username'])
        self.receiver['community'] = None
        return super(PioneerReferenceAddView, self).get_form(form_class)

    def get_context_data(self, *args, **kwargs):
        context = super(PioneerReferenceAddView, self).get_context_data(
            *args, **kwargs)
        context['pioneer'] = self.receiver['pioneer']
        context['page_title'] = _('Add reference for %(pioneer)s') % {
            'pioneer': self.receiver['pioneer'].username,
        }
        context['page_h1'] = _('Add reference')
        context['form_action'] = _('Add')
        return context

    def form_valid(self, form):
        result = super(PioneerReferenceAddView, self).form_valid(form)
        messages.success(self.request,
            _('The reference was successfully added.'))
        return result

    def get_success_url(self):
        return reverse('pioneer-detail', kwargs={
            'username': self.object.receiver_pioneer.username
        })

pioneer_reference_add = PioneerReferenceAddView.as_view()


class PioneerReferenceEditView(ReferenceEditView):
    template_name = 'ecobasa/pioneer_reference_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PioneerReferenceEditView, self).get_context_data(
            *args, **kwargs)
        context['pioneer'] = self.object.receiver_pioneer
        context['page_title'] = _('Edit reference for %(pioneer)s') % {
            'pioneer': self.object.receiver_pioneer.username,
        }
        context['page_h1'] = _('Edit reference')
        context['form_action'] = _('Edit')
        return context

    def form_valid(self, form):
        result = super(PioneerReferenceEditView, self).form_valid(form)
        messages.success(self.request,
            _('The reference was successfully edited.'))
        return result

    def get_success_url(self):
        return reverse('pioneer-detail', kwargs={
            'username': self.object.receiver_pioneer.username
        })

pioneer_reference_edit = PioneerReferenceEditView.as_view()


class PioneerReferenceListView(ListView):
    template_name = 'ecobasa/pioneer_reference_list.html'
    model = Reference

    def get(self, request, *args, **kwargs):
        self.pioneer = get_object_or_404(
            get_user_model(), username=self.kwargs['username'])
        return super(PioneerReferenceListView, self).get(
            request, *args, **kwargs)

    def get_queryset(self):
        qs = super(PioneerReferenceListView, self).get_queryset()
        return qs.filter(receiver_pioneer=self.pioneer)

    def get_context_data(self, *args, **kwargs):
        context = super(PioneerReferenceListView, self).get_context_data(
            *args, **kwargs)
        context['pioneer'] = self.pioneer
        return context

pioneer_reference_list = PioneerReferenceListView.as_view()
