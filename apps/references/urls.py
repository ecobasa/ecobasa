from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import Add, Edit


urlpatterns = patterns('',
    url(r'^add/(?P<receiver>[-_\w]+)/$',
        login_required(Add.as_view()), name='add'),
    url(r'^edit/(?P<pk>[-_\w]+)/$',
        login_required(Edit.as_view()), name='edit'),
)
