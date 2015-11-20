# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.utils.timezone import utc
from django.views.generic import ListView, DetailView, RedirectView

from extra_views import SortableListMixin

from cosinnus.models import CosinnusGroup
from cosinnus_note.models import Note
from cosinnus.views.mixins.group import FilterGroupMixin
from cosinnus.views.mixins.tagged import TaggedListMixin


class StartView(FilterGroupMixin, TaggedListMixin,
                   SortableListMixin, ListView):
    template_name = 'start.html'
    model = Note

    def get_queryset(self):
        # only public notes
        pk = getattr(settings, 'ECOBASA_GROUP', 1)
        try:
            group = CosinnusGroup.objects.filter(pk=pk)[0]
        except IndexError:
            return self.model.objects.none()
        else:
            qs = self.model.objects.filter(
                group=group, media_tag__public=True)[:3]
        qs = qs.prefetch_related('tags')
        if self.tag:
            qs = qs.filter(tags=self.tag)
        return qs

start = StartView.as_view()
