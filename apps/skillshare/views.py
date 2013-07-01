import json
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView, ListView, FormView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

from .models import Skill, SkillName
from .forms import get_form_badge, BadgeForm, SkillForm, SkillSearchForm

#############################################################################

class JSONResponseMixin(object):
    """A mixin that can be used to render a JSON response."""
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return HttpResponse(
            self.convert_context_to_json(context),
            content_type='application/json',
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        """Convert the context dictionary into a JSON object."""
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)

#############################################################################

class Index(TemplateView):
    template_name = 'skillshare/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        skills = []
        for name in SkillName.objects.order_by('name'):
            skills.append({
                'name': name.name,
                'slug': name.slug,
                'owners': [o.owner for o in name.skillshare_skill.all()],
            })
        context['skills'] = skills
        return context

#############################################################################

class Search(FormView):
    template_name = 'skillshare/search.html'
    form_class = SkillSearchForm

    def get_form(self, form_class):
        form = super(Search, self).get_form(form_class)
        names = SkillName.objects.values('name')
        form.fields['skillname'].choices = [(n['name'], n['name']) for n in names]
        return form


    def _get_multiple_choice_human(self, choices, values):
        default = _('Any')
        if not values:
            return default

        try:
            c = dict(choices)
            return ', '.join([c[v] for v in values])
        except KeyError:
            return default


    def form_valid(self, form):
        experience = form.cleaned_data['experience']
        sharetype = form.cleaned_data['sharetype']
        context = {
            'skillname': form.cleaned_data['skillname'],
            'experience': self._get_multiple_choice_human(Skill.CHOICES_EXPERIENCE, experience),
            'sharetype': self._get_multiple_choice_human(SkillSearchForm.CHOICES_SHARETYPE, sharetype),
            'form': form,
            'posted': True,
        }

        result = Skill.objects.filter(name__name__icontains=context['skillname'])
        if experience:
            result = result.filter(experience__in=experience)
        # don't have this specced yet
        # if sharetype:
        #     result = result.filter(sharetype__in=sharetype)
        context['result'] = result

        return TemplateResponse(self.request, self.template_name, context)

#############################################################################

class Detail(DetailView):
    model = Skill
    template_name = 'skillshare/detail.html'

    def get_object(self):
        return self.model.objects.get(
            name__slug=self.kwargs['slug'],
            owner__username=self.kwargs['owner'],
        )


    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)
        skill = context['object']
        return_url = reverse('skillshare:detail', kwargs= {
            'slug' : skill.name.slug,
            'owner': skill.owner.username,
        })
        skill.form_badge = get_form_badge(
            self.request, skill, return_url)

        context['can_edit'] = skill.can_edit(self.request.user)

        return context

#############################################################################

class Add(CreateView):
    template_name = 'skillshare/add.html'
    form_class = SkillForm

    def get_form_kwargs(self):
        kwargs = super(Add, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


    def get_context_data(self, **kwargs):
        context = super(Add, self).get_context_data(**kwargs)
        url = reverse('skillshare:ajax-available-owners', args=['0'])
        context['url_ajax_available_owners'] = url[:-2]
        return context


    def get_success_url(self):
        return reverse('skillshare:detail', kwargs={
            'slug': self.object.name.slug,
            'owner': self.object.owner.username,
        })


class AddForOwner(Add):
    def get_form_kwargs(self):
        kwargs = super(AddForOwner, self).get_form_kwargs()
        owner = get_object_or_404(User, username=self.kwargs['owner'])
        kwargs['initial']['owner'] = owner
        return kwargs


#############################################################################

class Edit(UpdateView):
    template_name = 'skillshare/edit.html'
    model = Skill
    form_class = SkillForm

    def get_object(self):
        skill = self.model.objects.get(
            name__slug=self.kwargs['slug'],
            owner__username=self.kwargs['owner'],
        )
        if skill.can_edit(self.request.user):
            return skill
        else:
            raise PermissionDenied


    def get_form_kwargs(self):
        kwargs = super(Edit, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


    def get_form(self, form_class):
        form = super(Edit, self).get_form(form_class)
        form.fields['name'].widget = forms.HiddenInput()
        form.fields['owner'].widget = forms.HiddenInput()
        return form


    def get_success_url(self):
        return reverse('skillshare:detail', kwargs={
            'slug': self.object.name.slug,
            'owner': self.object.owner.username,
        })

#############################################################################

class AvailableOwners(JSONResponseMixin, TemplateView):
    def render_to_response(self, context, **response_kwargs):
        owners = None
        if 'skillname' in context:
            try:
                skillname = int(context['skillname'])
            except ValueError:
                pass
            else:
                owners = User.objects.\
                    exclude(skillshare_skill_owner__name=skillname).\
                    values('pk', 'username')

        if not owners:
            owners = User.objects.all()

        context = {'available_owners': list(owners.values('pk', 'username'))}
        return self.render_to_json_response(context, **response_kwargs)

#############################################################################

class BadgeAdd(CreateView):
    template_name = 'skillshare/badge_add.html'
    form_class = BadgeForm

    def get_success_url(self):
        return_url = self.request.POST.get('return_url', None)
        if return_url:
            return return_url

        return reverse('skillshare:detail', kwargs={
            'slug': self.kwargs['slug'],
            'owner': self.kwargs['owner'],
        })


    def get_form(self, form_class):
        skill = get_object_or_404(
            Skill,
            name__slug=self.kwargs['slug'],
            owner__username=self.kwargs['owner']
        )
        form = get_form_badge(self.request, skill, None)
        if not form:
            raise PermissionDenied
        else:
            return form
