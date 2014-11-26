# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cosinnus.models import CosinnusGroupMembership


class OrganiserRoleManager(models.Manager):
    def for_user(self, user):
        qs = self.filter(cosinnus_group_membership__user=user)
        return qs.select_related('cosinnus_group_membership__group')


class OrganiserRole(models.Model):
    # links to user and group
    cosinnus_group_membership = models.ForeignKey(CosinnusGroupMembership,
        verbose_name=_('Cosinnus group membership'))
    title = models.CharField(
        verbose_name=_('Role title'),
        max_length=255)
    description = models.TextField(
        verbose_name=_('Role description'))

    objects = OrganiserRoleManager()

    class Meta:
        app_label = 'ecobasa'
        verbose_name = _('Organiser role')
        verbose_name_plural = _('Organiser roles')

    def __unicode__(self):
        return '%s: %s' % (
            self.cosinnus_group_membership.user.username, self.title)
