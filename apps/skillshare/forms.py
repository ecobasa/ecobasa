from django import forms
from django.utils.text import slugify
from django.utils.translation import ugettext as _

from .models import Badge, SkillName, Skill

#############################################################################

class SkillSearchForm(forms.Form):
    LEARN = 'LEA'
    TEACH = 'TEA'
    PARTNER = 'PAR'
    CHOICES_SHARETYPE = (
        (LEARN, _('Learn')),
        (TEACH, _('Teach')),
        (PARTNER, _('Partner')),
    )

    skillname = forms.ChoiceField(
        required=False,
        choices=(),
        label=_('Skill name'),
        help_text=_('What skill are you looking for?'),
    )
    experience = forms.MultipleChoiceField(
        required=False,
        choices=Skill.CHOICES_EXPERIENCE,
        widget=forms.CheckboxSelectMultiple(),
        label=_('Experience'),
        help_text=_('What level of experience are you looking for?'),
    )
    sharetype = forms.MultipleChoiceField(
        required=False,
        choices=CHOICES_SHARETYPE,
        widget=forms.CheckboxSelectMultiple(),
        label=_('Share type'),
        help_text=_('What kind of sharing experience are you looking for?'),
    )


#############################################################################
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SkillForm, self).__init__(*args, **kwargs)
        self.fields['creator'].widget = forms.HiddenInput()
        self.fields['experience'].widget = forms.RadioSelect(
            choices=Skill.CHOICES_EXPERIENCE)


    def _set_creator(self):
        # pin creator to request user
        # TODO: don't pin if creator already exists
        self.cleaned_data['creator'] = self.request.user
        if 'creator' in self._errors:
            self._errors.pop('creator')


    def _set_name(self):
        if 'name' in self.cleaned_data:
            return

        if self.request.method != 'POST':
            return

        name = self.request.POST.get('name', None)
        if not name:
            return

        slug = slugify(name)
        skillname, _ = SkillName.objects.get_or_create(name=name, slug=slug)
        self.cleaned_data['name'] = skillname
        self._errors.pop('name')
        # need to set self.data for preselection when presented to user
        data = self.data.copy()
        data['name'] = str(skillname.pk)
        self.data = data


    def clean(self):
        # set the 'name' and 'creator' after all validation has passed
        self._set_creator()
        self._set_name()
        return self.cleaned_data

#############################################################################

def get_form_badge(request, skill, return_url):
    user = request.user

    # no form if not authenticated
    if not user.is_authenticated():
        return None

    # no form if user's own skill
    if user == skill.owner:
        return None

    # no form if user has given already for this skill
    if skill.skillshare_badge.filter(giver=user):
        return None

    if request.method == 'POST':
        return BadgeForm(request.POST, request=request)
    else:
        initial={
            'skill' : skill,
            'giver': user,
            'return_url': return_url,
        }
        return BadgeForm(initial=initial, request=request)


#############################################################################

class BadgeForm(forms.ModelForm):
    return_url = forms.CharField(required=False,
        widget=forms.HiddenInput)

    class Meta:
        model = Badge
        fields = ['skill', 'giver', 'feedback']


    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(BadgeForm, self).__init__(*args, **kwargs)
        self.fields['skill'].widget = forms.HiddenInput()
        self.fields['giver'].widget = forms.HiddenInput()


    def clean_giver(self):
        giver = self.cleaned_data['giver']

        if giver != self.request.user: # force request.user to be giver
            giver = self.request.user

        if not giver.is_authenticated(): # don't add badge if not authenticated
            raise forms.ValidationError(
                _('You must be authenticated to give a badge.'))

        return giver


    def clean_skill(self):
        skill = self.cleaned_data['skill']
        if skill.owner == self.request.user:
            raise forms.ValidationError(
                _('Cannot add a badge for your own skill.'))
        else:
            return skill
