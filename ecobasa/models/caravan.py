# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

from cosinnus.models import (
    BaseUserProfile, BaseUserProfileManager, CosinnusGroup)


class TaggedOffer(TaggedItemBase):
    content_object = models.ForeignKey('Caravan')

    class Meta:
        app_label = 'ecobasa'

@python_2_unicode_compatible
class Caravan(CosinnusGroup):
    avatar = ThumbnailerImageField(_('avatar'),
        upload_to='caravans', null=True, blank=True)
    offers = TaggableManager(_('offers'),
        through=TaggedOffer, related_name='_offer', blank=True,
        help_text='Anything useful for communites that you can take with you on your caravan (clay, tools, music, books..')

    class Meta:
        app_label = 'ecobasa'
        ordering = ('name',)
        verbose_name = _('Caravan')
        verbose_name_plural = _('Caravans')

    def __str__(self):
        return self.name
