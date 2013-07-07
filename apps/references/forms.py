from django import forms
from django.utils.translation import ugettext as _

from .models import Reference

#############################################################################

class ReferenceForm(forms.ModelForm):
    return_url = forms.CharField(required=False,
        widget=forms.HiddenInput)

    class Meta:
        model = Reference

    def __init__(self, *args, **kwargs):
        super(ReferenceForm, self).__init__(*args, **kwargs)
        self.fields['giver'].widget = forms.HiddenInput()
        self.fields['receiver'].widget = forms.HiddenInput()

#############################################################################

def get_form(request, receiver, return_url):
    user = request.user

    # no form if not authenticated
    if not user.is_authenticated():
        return None

    # no form if receiver is same as user
    if user == receiver:
        return None

    # no form if user has given already for this skill
    if Reference.objects.filter(giver=user, receiver=receiver):
        return None

    if request.method == 'POST':
        return ReferenceForm(request.POST)
    else:
        initial={
            'giver': user,
            'receiver': receiver,
            'return_url': return_url,
        }
        return ReferenceForm(initial=initial)



