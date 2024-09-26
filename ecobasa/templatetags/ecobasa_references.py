# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from random import sample

from ..models import Reference
register = template.Library()


@register.assignment_tag
def get_random_references():
    # fetch all positive references
    positive_references = Reference.objects.filter(recommend=True)
    
    # get 3 random positive references
    random_references = sample(list(positive_references), 3)

    return random_references
