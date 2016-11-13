# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from cosinnus_note.models import Note

register = template.Library()


@register.inclusion_tag('ecobasa/blog_post_list.html', takes_context=True)
def show_posts(context, tags):
    
    # only public notes
    qs = Note.objects.filter(media_tag__public=True)
    qs = qs.prefetch_related('tags')
    if tags:
        qs = qs.filter(tags=tags)

    posts = []
    for post in qs.select_related('group', 'group__caravan'):
        if hasattr(post.group, 'caravan'):
           posts.append(post)
    context['object_list'] = posts

    return context