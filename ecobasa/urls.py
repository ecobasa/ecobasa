from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

admin.autodiscover()


urlpatterns = i18n_patterns('',
    url(r'^accounts/register/$',
        'ecobasa.views.register', name='register'),
    url(r'^accounts/register/community',
        'ecobasa.views.register_community', name='register-community'),
    url(r'^accounts/register/member',
        'ecobasa.views.register_member', name='register-member'),
    url(r'^accounts/', include('cosinnus.utils.django_auth_urls')),
    url(r'^accounts/', include('userprofiles.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

    url(r'^communities/$', 'ecobasa.views.community_list', name='community-list'),
    url(r'^community/(?P<group>[^/]+)/$', 'ecobasa.views.community_dashboard', name='community-dashboard'),
    url(r'^community/(?P<group>[^/]+)/details/$', 'ecobasa.views.community_detail', name='community-detail'),
    url(r'^community/(?P<group>[^/]+)/edit/$', 'ecobasa.views.community_update', name='community-edit'),

    url(r'^pioneers/$', 'ecobasa.views.pioneer_list', name='pioneer-list'),
    url(r'^pioneer/(?P<username>[^/]+)/$', 'ecobasa.views.pioneer_detail', name='pioneer-detail'),

    url(r'^buses/$', 'ecobasa.views.bus_list', name='bus-list'),
    url(r'^bus/add/$', 'ecobasa.views.bus_add', name='bus-add'),

    # url(r'^skillshare/', include('skillshare.urls', namespace='skillshare')),
    # url(r'^references/', include('references.urls', namespace='references')),

    url(r'^$', 'cms.views.details', {'slug': ''}),
)


# language-independent patterns
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

urlpatterns += patterns('',
    (r'^i18n/', include('django.conf.urls.i18n')),
)


# catch-all patterns
urlpatterns += i18n_patterns('',
    url(r'^', include('cosinnus.urls', namespace='cosinnus')),
    url(r'^', include('cms.urls')),
)
