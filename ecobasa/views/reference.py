# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView

from ..forms import ReferenceForm, get_form
from ..models import (Reference,
    TaggedReferenceProduct, TaggedReferenceService, TaggedReferenceSkill)


def get_tag_counts(references):
    """
    The idea is to have a dict (of tag_type-specific dicts) with the name
    of the tag and the count how often the receiver received a reference with
    that tag.
    The argument should be a list (or queryset) of references for a specific
    receiver.
    For convenience, an item also includes a Bootstrap CSS class which can be
    used in the template for different background colors.
    The output will look a bit like:
    {
        'products': {
            'pr_tag1': {
                'count': 1,
                'class': 'primary',
            },
            'pr_tag2': {
                'count': 2,
                'class': 'success',
            },
        },
        'services': {
            'se_tag1': {
                'count': 42,
                'class': 'primary',
            },
        },
        'skills': {
        }
    }
    """
    classes = ['primary', 'success', 'info', 'warning', 'danger']
    classes_len = len(classes)

    def _tag_counts_model(references, model):
        """Here the model-/tag_tag-specific collection is computed."""
        classes_current = 0
        tags = {}
        tagged_references = model.objects.filter(
            content_object__in=references).select_related('tag')
        for tagged_reference in tagged_references:
            tag = tagged_reference.tag
            if tag.name not in tags:
                tags[tag.name] = {
                    'class': classes[classes_current],
                    'count': 1,
                }
                classes_current = (classes_current + 1) % classes_len
            else:
                tags[tag.name]['count'] += 1
        return tags

    tags = {
        'products': _tag_counts_model(references, TaggedReferenceProduct),
        'services': _tag_counts_model(references, TaggedReferenceService),
        'skills': _tag_counts_model(references, TaggedReferenceSkill),
    }
    return tags


class ReferenceAddView(CreateView):
    form_class = ReferenceForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ReferenceAddView, self).dispatch(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(ReferenceAddView, self).__init__(*args, **kwargs)
        self.receiver = {}

    def get_form(self, form_class):
        form = get_form(self.request, self.receiver)
        if not form:
            raise PermissionDenied
        else:
            return form

reference_add = ReferenceAddView.as_view()


class ReferenceEditView(UpdateView):
    model = Reference
    form_class = ReferenceForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ReferenceEditView, self).dispatch(*args, **kwargs)

    def get_object(self):
        obj = super(ReferenceEditView, self).get_object()
        user = self.request.user
        if user != obj.giver and not user.is_superuser:
            raise PermissionDenied
        else:
            return obj

reference_edit = ReferenceEditView.as_view()
