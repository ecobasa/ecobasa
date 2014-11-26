# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from cosinnus.views.profile import UserProfileUpdateView
from cosinnus.views.user import UserListView


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
