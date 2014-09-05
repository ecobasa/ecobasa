# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.utils.html import escape

from cosinnus_message.forms import CustomWriteForm as CosinnusWriteForm

import six


class CustomWriteForm(CosinnusWriteForm):
    """The form for an authenticated user, to compose a message.

    REMOVE THIS FILE ONCE cosinnus-message gets updated to current version!
    """
    def __init__(self, *args, **kwargs):
        super(CustomWriteForm, self).__init__(*args, **kwargs)
        
        # retrieve the attached objects ids to select them in the update view
        users = []
        initial_users = kwargs['initial'].get('recipients', None)
        if initial_users:
            for username in initial_users.split(', '):
                users.append( get_user_model()._default_manager.get(username=username) )
                # delete the initial data or our select2 field initials will be overwritten by django
                del kwargs['initial']['recipients']
                del self.initial['recipients']
                
            # TODO: sascha: returning unescaped html here breaks the javascript of django-select2
            preresults = [("user:" + six.text_type(user.id), escape(user.username),)#render_to_string('cosinnus_message/user_select_pill.html', {'type':'user','text':escape(user.first_name) + " " + escape(user.last_name)}),)
                       for user in users]
            
            # we need to cheat our way around select2's annoying way of clearing initial data fields
            self.fields['recipients'].choices = preresults #((1, 'hi'),)
            self.fields['recipients'].initial = [key for key,val in preresults] #[1]
