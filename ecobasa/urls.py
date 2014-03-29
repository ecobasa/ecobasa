from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

admin.autodiscover()


urlpatterns = i18n_patterns('',
    url(r'^accounts/register/community',
        'ecobasa.views.register_community', name='register-community'),
    url(r'^accounts/register/member',
        'ecobasa.views.register_member', name='register-member'),
    url(r'^accounts/', include('cosinnus.utils.django_auth_urls')),
    url(r'^accounts/', include('userprofiles.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

    url(r'^group/(?P<group>[^/]+)/$', 'ecobasa.views.group_index', name='group-index'),
    url(r'^group/(?P<group>[^/]+)/details/$', 'ecobasa.views.group_detail', name='group-detail'),
    url(r'^groups/$', 'ecobasa.views.group_list', name='group-list'),

    # url(r'^skillshare/', include('skillshare.urls', namespace='skillshare')),
    # url(r'^references/', include('references.urls', namespace='references')),

    url(r'^$', 'cms.views.details', {'slug': ''}),
)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )


# catch-all patterns
urlpatterns += i18n_patterns('',
    url(r'^', include('cosinnus.urls', namespace='cosinnus')),
    url(r'^', include('cms.urls')),
)
