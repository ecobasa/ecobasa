# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.utils.datastructures import SortedDict
from cosinnus.models.profile import get_user_profile_model
from cosinnus.models.serializers.profile import BaseUserProfileSerializer

class EcobasaUserProfileSerializer(BaseUserProfileSerializer):

    class Meta(BaseUserProfileSerializer.Meta):
        model = get_user_profile_model()

    def get_fields(self):
        """
        Overwriting this, because otherwise we get a:

        Cannot set required=True and read_only=True

        /ecobasa/lib/python2.7/site-packages/rest_framework/fields.py in __init__
        assert not (read_only and required), "Cannot set required=True and read_only=True"

        coming from:
        /ecobasa/src/cosinnus/cosinnus/models/serializers/profile.py in UserSimpleSerializer
        profile = _UserProfileSerializer(source='cosinnus_profile', many=False, read_only=True)

        Since we don't need this whole serialisation at the moment, this sort
        it fixes the issue. Once we want to use serialisation, remove this and
        implement this class properly. TODO
        """
        return SortedDict()

