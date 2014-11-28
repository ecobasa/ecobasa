# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.utils.timezone import utc
from django.views.generic import ListView, DetailView, RedirectView

from cosinnus.models import CosinnusGroup
from cosinnus_note.models import Note


class AboutView(ListView):
    template_name = 'ecobasa/about.html'
    model = Note

    def __init__(self, *args, **kwargs):
        super(AboutView, self).__init__(*args, **kwargs)
        self.start = datetime.datetime(*settings.ECOBASA_TOUR_START, tzinfo=utc)
        self.end = datetime.datetime(*settings.ECOBASA_TOUR_END, tzinfo=utc)

    def get_queryset(self):
        # only public notes
        qs = self.model.objects.filter(media_tag__public=True)
        # only within tour start and end
        qs = qs.filter(created__gte=self.start, created__lte=self.end)
        return qs

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context.update({
            'tour_start': self.start,
            'tour_end': self.end,
        })
        return context

about = AboutView.as_view()
