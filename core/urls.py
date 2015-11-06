from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^user/', include('registration.backends.simple.urls')),
    url(r'^user/', include('django.contrib.auth.urls')),
    url(r'^school/create/$', SchoolCreateView.as_view(), name='school_create'),
    url(r'school/$', SchoolListView.as_view(), name='school_list'),
    url(r'^school/(?P<pk>\d+)/$', SchoolDetailView.as_view(), name='school_detail'),
)