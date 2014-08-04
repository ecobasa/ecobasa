# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cosinnus.models import CosinnusGroup


@python_2_unicode_compatible
class Caravan(CosinnusGroup):
    class Meta:
        app_label = 'ecobasa'
        ordering = ('name',)
        verbose_name = _('Caravan')
        verbose_name_plural = _('Caravans')

    def __str__(self):
        return self.name

from ecobasa.models import mail_patch_postman