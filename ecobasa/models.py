# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from cosinnus.models import BaseUserProfile, BaseUserProfileManager


class EcobasaUserProfile(BaseUserProfile):
    myfield = models.CharField('myfield', max_length=10)

    objects = BaseUserProfileManager()
