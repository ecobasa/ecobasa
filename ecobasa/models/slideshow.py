# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField


class SlideshowPlugin(CMSPlugin):
    name = models.CharField(verbose_name=_("name"), max_length=100)

    def __unicode__(self):
        return u"%s" % (self.name,)

    @property
    def height(self):
        max_height = 0
        for image in self.images.all():
            max_height = max(max_height, image.file.height)
        return max_height

    class Meta:
        app_label = 'ecobasa'
        verbose_name = _("slide show")
        verbose_name_plural = _("slide shows")

    def copy_relations(self, oldinstance):
        for image in oldinstance.images.all():
            image.pk = None
            image.slideshow = self
            image.save()


class Linkable(object):
    @property
    def link(self):
        if self.link_url:
            return self.link_url
        elif self.link_page:
            return self.link_page.get_absolute_url()
        elif self.link_article:
            return self.link_article.get_absolute_url()
        return "#"


class SlideshowImage(Linkable, models.Model):
    slideshow = models.ForeignKey(SlideshowPlugin, verbose_name=_("slide show"), related_name="images")
    file = FilerImageField(verbose_name=_("file"), null=True, blank=True)
    title = models.CharField(verbose_name=_("title"), max_length=255, blank=True)
    text = models.TextField(verbose_name=_("text"), max_length=255, blank=True, help_text=_("Text appearing on top of the image"))
    order = models.PositiveSmallIntegerField(verbose_name=_("order"), default=0)

    def __unicode__(self):
        return u"%s slideshow image" % (self.slideshow,)

    class Meta:
        app_label = 'ecobasa'
        verbose_name = _("image")
        verbose_name_plural = _("images")
        ordering = ('order', 'id',)
