from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from ecobasa.views import HomeView, ProfileView


urlpatterns = patterns('',
    # url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^profile/(?P<slug>[-_\w]+)/$', ProfileView.as_view(), name='profile'),

    url(r'^accounts/', include('cosinnus.utils.django_auth_urls')),
    url(r'^accounts/', include('userprofiles.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^skillshare/', include('skillshare.urls', namespace='skillshare')),
    # url(r'^references/', include('references.urls', namespace='references')),
    url(r'^', include('cosinnus.urls', namespace='cosinnus')),
)
