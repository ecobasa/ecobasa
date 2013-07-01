from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from skillshare import get_skills_for_owner


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['users'] = User.objects.filter(is_superuser=False)
        return context


class ProfileView(DetailView):
    model = User
    slug_field = 'username'
    template_name = 'profile.html'


    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        return_url = reverse('profile', kwargs={'slug' : context['object']})
        context['skills'] = get_skills_for_owner(
            self.request, context['object'], return_url)
        return context

