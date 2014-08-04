# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, RedirectView

from cosinnus.models import CosinnusGroup
from cosinnus_note.models import Note

class NoteListView(ListView):
    template_name = 'about.html'
    queryset = Note.objects.all()

    def get_context_data(self, **kwargs):
        context = super(NoteListView, self).get_context_data(**kwargs)
        context.update({'posts': Note.objects.all()})
        return context

note_list = NoteListView.as_view()
