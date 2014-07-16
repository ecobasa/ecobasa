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

from cosinnus.models.group import MEMBERSHIP_ADMIN
from cosinnus.views.user import UserListView, USER_MODEL
from cosinnus_note.models import Note

from ..forms import PioneerProfileForm


class PioneerListView(UserListView):
    template_name = 'ecobasa/pioneer_list.html'

    def get_queryset(self):
        users = super(PioneerListView, self).get_queryset()
        # exclude ambassadors, but include organisers (even if ambassador)
        # you are welcome to get this into one query
        # pioneers = users.exclude(
        #            cosinnus_memberships__status=MEMBERSHIP_ADMIN,
        #            cosinnus_memberships__organiserrole__isnull=True,
        #        )
        # didn't do it.
        organisers = list(users.filter(
            cosinnus_memberships__organiserrole__isnull=False).distinct())
        non_ambassadors = list(users.exclude(
            cosinnus_memberships__status=MEMBERSHIP_ADMIN))
        pioneers = set(organisers + non_ambassadors)
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
        context = super(PioneerDetailView, self).get_context_data(*args,
                                                                  **kwargs)
        context['posts'] = Note.objects.filter(creator=context['object'])
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
