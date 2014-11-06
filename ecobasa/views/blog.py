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
from cosinnus.views.mixins.tagged import TaggedListMixin


class BlogView(ListView, TaggedListMixin):
    template_name = 'ecobasa/blog.html'
    model = Note

    def __init__(self, *args, **kwargs):
        super(BlogView, self).__init__(*args, **kwargs)

    def get_queryset(self):
        # only public notes
        qs = self.model.objects.filter(media_tag__public=True)
        return qs

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        return context

blog = BlogView.as_view()
