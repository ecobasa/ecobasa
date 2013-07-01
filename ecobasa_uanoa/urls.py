from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from ecobasa_uanoa.views import HomeView, ProfileView


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^profile/(?P<slug>[-_\w]+)/$', ProfileView.as_view(), name='profile'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^skillshare/', include('skillshare.urls', namespace='skillshare')),
)
