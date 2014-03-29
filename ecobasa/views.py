from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, RedirectView, DetailView
from cosinnus.views.mixins.group import RequireReadMixin
from cosinnus.views.group import GroupDetailView, GroupListView
from cosinnus.views.profile import UserProfileDetailView
from cosinnus.views.user import UserListView
from userprofiles.views import RegistrationView

from .forms import (
    EcobasaRegistrationMemberForm, EcobasaRegistrationCommunityForm)


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


#############################################################################
# registration overrides
#############################################################################

class EcobasaRegistrationMemberView(RegistrationView):
    template_name = 'userprofiles/registration_member.html'
    form_class = EcobasaRegistrationMemberForm
register_member = EcobasaRegistrationMemberView.as_view()


class EcobasaRegistrationCommunityView(RegistrationView):
    template_name = 'userprofiles/registration_community.html'
    form_class = EcobasaRegistrationCommunityForm
register_community = EcobasaRegistrationCommunityView.as_view()

