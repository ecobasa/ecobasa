from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, RedirectView, DetailView
from cosinnus.views.mixins.group import RequireReadMixin
from cosinnus.views.group import GroupDetailView, GroupListView
from cosinnus.views.profile import UserProfileDetailView
from cosinnus.views.user import UserListView

from skillshare import get_skills_for_owner
from references import get_references_for_receiver



class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['users'] = User.objects.filter(is_superuser=False)
        return context


# class ProfileView(DetailView):
#     model = User
#     slug_field = 'username'
#     template_name = 'profile.html'

#     def get_context_data(self, **kwargs):
#         context = super(ProfileView, self).get_context_data(**kwargs)
#         return_url = reverse('profile', kwargs={'slug': context['object']})
#         context['skills'] = get_skills_for_owner(
#             self.request, context['object'], return_url)
#         context['references'], context['reference_form'] = \
#             get_references_for_receiver(self.request, context['object'],
#             return_url)
#         return context


class EcobasaProfileView(UserProfileDetailView):
    def get_context_data(self, **kwargs):
        context = super(EcobasaProfileView, self).get_context_data(**kwargs)
        context['profile'] = self.object.profile
        return context
user_detail = EcobasaProfileView.as_view()


class GroupIndexView(RequireReadMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('cosinnus:group-detail', kwargs={'group': self.group.slug})
group_index = GroupIndexView.as_view()


class EcobasaGroupDetailView(GroupDetailView):
    def get_context_data(self, **kwargs):
        context = super(EcobasaGroupDetailView, self).get_context_data(**kwargs)
        context['profile'] = self.object.profile
        return context
group_detail = EcobasaGroupDetailView.as_view()


class EcobasaGroupListView(GroupListView):
    def get_context_data(self, **kwargs):
        context = super(EcobasaGroupListView, self).get_context_data(**kwargs)
        return context
group_list = EcobasaGroupListView.as_view()

class BusListView(UserListView):
    template_name = 'buslist.html'
    def get_context_data(self, **kwargs):
        context = super(BusListView, self).get_context_data(**kwargs)
        return context
bus_list = BusListView.as_view()
