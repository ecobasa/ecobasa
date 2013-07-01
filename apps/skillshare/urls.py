from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import Index, Search, Detail, Add, AddForOwner, Edit, AvailableOwners, BadgeAdd


urlpatterns = patterns('skills.views',
    url(r'^$', Index.as_view(), name='index'),
    url(r'^search/$', Search.as_view(), name='search'),
    url(r'^add/$',
        login_required(Add.as_view()), name='add'),
    url(r'^add/(?P<owner>[-_\w]+)/$',
        login_required(AddForOwner.as_view()), name='add-for-owner'),
    url(r'^ajax/available-owners/$', # to get available owners for new skill
        AvailableOwners.as_view(), name='ajax-available-owners'),
    url(r'^ajax/available-owners/(?P<skillname>[-_\w]+)/$',
        AvailableOwners.as_view(), name='ajax-available-owners'),
    url(r'^(?P<slug>[-_\w]+)/(?P<owner>[-_\w]+)/$',
        Detail.as_view(), name='detail'),
    url(r'^(?P<slug>[-_\w]+)/(?P<owner>[-_\w]+)/edit/$',
        login_required(Edit.as_view()), name='edit'),
    url(r'^(?P<slug>[-_\w]+)/(?P<owner>[-_\w]+)/badge/add/$',
        login_required(BadgeAdd.as_view()), name='badge-add'),
)
