# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.inclusion_tag('ecobasa/start_blog_post.html', takes_context=True)
def show_start_post(context, post):
    group = post.group
    if hasattr(group, 'caravan'):
        urlname = 'caravan-detail'
    elif hasattr(group, 'profile'):
        urlname = 'community-detail'
    else:
        urlname = 'cosinnus:group-detail'
    group_url = reverse(urlname, kwargs={'group': group.slug})

    context.update({
        'post': post,
        'pioneer_url': reverse('pioneer-detail', kwargs={
            'username': post.creator.get_username}),
        'group_url': group_url
    })
    return context
