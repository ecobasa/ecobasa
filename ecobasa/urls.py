from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from haystack.views import search_view_factory
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView

from .views import FindView

admin.autodiscover()


urlpatterns = i18n_patterns('',
    #url(_(r'^about/$'), 'ecobasa.views.about', name='about'),
    url(r'^blog/$', 'ecobasa.views.blog', name='blog'),
    url(r'^blog/(?P<tag>[^/]+)/$', 'ecobasa.views.blog', name='blog_filtered'),
    # url(r'^community-tours/blog/$', 'ecobasa.views.tour_blog', name='tour_blog'),
    # url(r'^community-tours/blog/(?P<tag>[^/]+)/$', 'ecobasa.views.tour_blog', name='tour_blog_filtered'),
    url(r'^accounts/register/$',
        'ecobasa.views.register', name='register'),
    url(r'^accounts/register/community',
        'ecobasa.views.register_community', name='register-community'),
    url(r'^accounts/register/member',
        'ecobasa.views.register_member', name='register-member'),
    url(r'^accounts/', include('cosinnus.utils.django_auth_urls')),
    url(r'^accounts/', include('userprofiles.urls')),
    url(r'', include('django_browserid.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

    url(r'^communities/$', 'ecobasa.views.community_list', name='community-list'),
    url(r'^communities/(?P<group>[^/]+)/$', 'ecobasa.views.community_detail', name='community-detail'),
    url(r'^communities/(?P<group>[^/]+)/edit/$', 'ecobasa.views.community_update', name='community-edit'),
    url(r'^communities/(?P<group>[^/]+)/dashboard/$', 'ecobasa.views.community_dashboard', name='community-dashboard'),
    url(r'^communities/(?P<group>[^/]+)/reference/$',
        'ecobasa.views.community_reference_list', name='community-reference-list'),
    url(r'^communities/(?P<group>[^/]+)/reference/add/$',
        'ecobasa.views.community_reference_add', name='community-reference-add'),
    url(r'^communities/(?P<group>[^/]+)/reference/(?P<pk>\d+)/edit/$',
        'ecobasa.views.community_reference_edit', name='community-reference-edit'),

    url(r'^pioneers/$', 'ecobasa.views.pioneer_list', name='pioneer-list'),
    url(r'^pioneers/(?P<username>[^/]+)/$', 'ecobasa.views.pioneer_detail', name='pioneer-detail'),
    url(r'^pioneers/(?P<username>[^/]+)/edit/$', 'ecobasa.views.pioneer_update', name='pioneer-edit'),
    url(r'^pioneers/(?P<username>[^/]+)/reference/$',
        'ecobasa.views.pioneer_reference_list', name='pioneer-reference-list'),
    url(r'^pioneers/(?P<username>[^/]+)/reference/add/$',
        'ecobasa.views.pioneer_reference_add', name='pioneer-reference-add'),
    url(r'^pioneers/(?P<username>[^/]+)/reference/(?P<pk>\d+)/edit/$',
        'ecobasa.views.pioneer_reference_edit', name='pioneer-reference-edit'),

    url(r'^community-tours/buses/$', 'ecobasa.views.bus_list', name='bus-list'),
    url(r'^community-tours/buses/add/$', 'ecobasa.views.bus_add', name='bus-add'),

    url(r'^community-tours/tours/$', 'ecobasa.views.caravan_list', name='caravan-list'),
    url(r'^community-tours/tours/add/$', 'ecobasa.views.caravan_add', name='caravan-add'),
    url(r'^community-tours/tours/(?P<group>[^/]+)/$', 'ecobasa.views.caravan_detail', name='caravan-detail'),
    url(r'^community-tours/tours/(?P<group>[^/]+)/dashboard/$', 'ecobasa.views.caravan_dashboard', name='caravan-dashboard'),
    url(r'^community-tours/tours/(?P<group>[^/]+)/edit/$', 'ecobasa.views.caravan_edit', name='caravan-edit'),
    url(r'^community-tours/tours/(?P<group>[^/]+)/delete/$', 'ecobasa.views.caravan_delete', name='caravan-delete'),
    url(r'^community-tours/tours/(?P<group>[^/]+)/join/$', 'ecobasa.views.caravan_join', name='caravan-join'),
    url(r'^community-tours/tours/(?P<group>[^/]+)/leave/$', 'ecobasa.views.caravan_leave', name='caravan-leave'),

    url(r'^find/$', search_view_factory(view_class=FindView), name='find'),

    url(r'^organisers/$', 'ecobasa.views.organiser_list', name='organiser-list'),
    url(r'^team/$', 'ecobasa.views.organiser_list', name='organiser-list'),
    # url(r'^skillshare/', include('skillshare.urls', namespace='skillshare')),

    url(r'^messages/', include('cosinnus_message.postman_urls')),

    url(r'^contact/', include('contact_form.urls')),

    url(r'^$', 'cms.views.details', {'slug': ''}),

    url(_(r'^about/$'), RedirectView.as_view(url='/about-the-platform/'), name='about'),
    url(_(r'^info/$'), RedirectView.as_view(url='/about-the-platform/'), name='about'),
)


urlpatterns += patterns('',
    (r'^i18n/', include('django.conf.urls.i18n')),
)


# catch-all patterns
urlpatterns += i18n_patterns('',
    url(r'^', include('cosinnus.urls', namespace='cosinnus')),
    url(r'^', include('cms.urls')),
)

#url(r'^select2/', include('django_select2.urls')),
