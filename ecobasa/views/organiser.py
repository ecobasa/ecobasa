# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView

from ..models import OrganiserRole


class OrganiserListView(ListView):
    model = OrganiserRole
    template_name = 'ecobasa/organiser_list.html'

organiser_list = OrganiserListView.as_view()
