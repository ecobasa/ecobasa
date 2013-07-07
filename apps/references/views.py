import json
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView

from .models import Reference
from .forms import ReferenceForm, get_form

#############################################################################

class Add(CreateView):
    template_name = 'references/add.html'
    form_class = ReferenceForm

    def get_form(self, form_class):
        receiver = get_object_or_404(User, username=self.kwargs['receiver'])
        form = get_form(self.request, receiver, None)
        if not form:
            raise PermissionDenied
        else:
            return form


    def get_success_url(self):
        return_url = self.request.POST.get('return_url', None)
        if return_url:
            return return_url

        return reverse('profile', kwargs={
            'slug': self.object.receiver
        })

#############################################################################

class Edit(UpdateView):
    template_name = 'references/edit.html'
    model = Reference
    form_class = ReferenceForm

    def get_success_url(self):
        return reverse('profile', kwargs={
            'slug': self.object.receiver
        })
