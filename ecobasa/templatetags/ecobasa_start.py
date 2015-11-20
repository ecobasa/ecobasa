# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.core.urlresolvers import reverse

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

register = template.Library()

@register.assignment_tag
def show_start_post(context, post):

    model = Note

    # only public notes
    pk = getattr(settings, 'ECOBASA_GROUP', 1)
    try:
        group = CosinnusGroup.objects.filter(pk=pk)[0]
    except IndexError:
        return self.model.objects.none()
    else:
        context = self.model.objects.filter(
            group=group, media_tag__public=True)[:3]

    group_url = reverse(urlname, kwargs={'group': group.slug})

    context.update({
        'post': post,
        'pioneer_url': reverse('pioneer-detail', kwargs={
            'username': post.creator.get_username}),
        'group_url': group_url
    })
    return context
    