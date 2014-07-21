# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, RedirectView

from cosinnus.models.group import CosinnusGroupMembership, MEMBERSHIP_MEMBER
from cosinnus.utils.compat import atomic
from cosinnus.views.group import (
    GroupDetailView, GroupCreateView, GroupUpdateView, GroupDeleteView)
from cosinnus.views.widget import DashboardMixin

from ..forms import CaravanForm
from ..models import Caravan

from cosinnus.models import CosinnusGroup
from cosinnus.models.group import MEMBERSHIP_ADMIN, MEMBERSHIP_PENDING
from cosinnus.views.group import GroupListView
from cosinnus.views.widget import DashboardMixin
from cosinnus_note.models import Note

from ecobasa.views.bus import BusListView


class CaravanListView(ListView):
    template_name = 'ecobasa/caravan_list.html'
    queryset = Caravan.objects.filter(public=True)

caravan_list = CaravanListView.as_view()


class CaravanAddView(GroupCreateView):
    model = Caravan
    form_class = CaravanForm

    # enable any logged in user to create a caravan
    @method_decorator(login_required)
    @atomic
    def dispatch(self, *args, **kwargs):
        # yes, call super of super
        return super(GroupCreateView, self).dispatch(*args, **kwargs)

    def get_form(self, form_class):
        form = super(CaravanAddView, self).get_form(form_class)
        # make caravan public by default
        form.forms['obj'].initial['public'] = True
        return form

    def get_success_url(self):
        return reverse('caravan-detail', kwargs={'group': self.object.slug})

caravan_add = CaravanAddView.as_view()


class CaravanEditView(GroupUpdateView):
    model = Caravan
    form_class = CaravanForm

    def get_success_url(self):
        return reverse('caravan-detail', kwargs={'group': self.object.slug})

caravan_edit = CaravanEditView.as_view()


class CaravanDetailView(GroupDetailView):
    model = Caravan
    template_name = 'ecobasa/caravan_detail.html'

    def get_filter(self):
        return {'group_id': self.object.pk}

    def get_context_data(self, **kwargs):
        context = super(CaravanDetailView, self).get_context_data(**kwargs)


caravan_detail = CaravanDetailView.as_view()


class CaravanDashboardView(DashboardMixin, DetailView):
    """Not really useful yet."""
    model = Caravan
    slug_url_kwarg = 'group'
    context_object_name = 'group'

    def get_filter(self):
        return {'group_id': self.object.pk}

caravan_dashboard = CaravanDashboardView.as_view()


class CaravanDeleteView(GroupDeleteView):
    model = Caravan

    def get_success_url(self):
        return reverse('caravan-list')

caravan_delete = CaravanDeleteView.as_view()


class CaravanJoinView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        caravan = Caravan.objects.get(slug=kwargs['group'])
        CosinnusGroupMembership.objects.create(
            user=self.request.user,
            group=caravan,
            status=MEMBERSHIP_MEMBER,
        )
        return reverse('caravan-list')

caravan_join = CaravanJoinView.as_view()


class CaravanLeaveView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        caravan = Caravan.objects.get(slug=kwargs['group'])
        try:
            membership = CosinnusGroupMembership.objects.get(
                user=self.request.user,
                group=caravan,
            )
            membership.delete()
        except CosinnusGroupMembership.DoesNotExist:
            pass
        return reverse('caravan-list')

caravan_leave = CaravanLeaveView.as_view()
