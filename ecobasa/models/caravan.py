# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

from cosinnus.models import CosinnusGroup



class TaggedOffers(TaggedItemBase):
    content_object = models.ForeignKey('Caravan')

    class Meta:
        app_label = 'ecobasa'


@python_2_unicode_compatible
class Caravan(CosinnusGroup):
    offers = TaggableManager(
        verbose_name=_('Offers'),
        help_text=_('If the caravan collects something on the way for example, communities know what it is coming with. Connect two words with a "-" to have one tag.'),
        blank=True,
        through=TaggedOffers)
    image = ThumbnailerImageField(
        verbose_name=_('Image'),
        help_text=_('An image of the caravan.'),
        upload_to='caravans',
        null=True,
        blank=True)

    class Meta:
        app_label = 'ecobasa'
        ordering = ('name',)
        verbose_name = _('Caravan')
        verbose_name_plural = _('Caravans')

    def __str__(self):
        return self.name

#from ecobasa.models import mail_patch_postman
