# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cosinnus.models.profile import get_user_profile_model
from cosinnus.models.serializers.profile import BaseUserProfileSerializer


class EcobasaUserProfileSerializer(BaseUserProfileSerializer):

    class Meta(BaseUserProfileSerializer.Meta):
        model = get_user_profile_model()
