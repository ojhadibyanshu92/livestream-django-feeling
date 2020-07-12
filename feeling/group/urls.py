from django.conf.urls import url, include

from . import views
from .views import company,family

company_patterns = [

    url(r'^create/$', views.company.Create.as_view(), name='create'),
    url(r'^invites/$', company.Invites.as_view(), name='invites'),
    url(r'^edit/(?P<slug>[-\w]+)/$', views.company.Update.as_view(), name='update'),
    url(r'^view/(?P<slug>[-\w]+)/$', views.company.Detail.as_view(), name='detail'),

]
family_patterns = [

    url(r'^create/$', views.family.Create.as_view(), name='create'),
    url(r'^edit/(?P<slug>[-\w]+)/$', views.family.Update.as_view(), name='update'),
    url(r'^view/(?P<slug>[-\w]+)/$', views.family.Detail.as_view(), name='detail'),

]

urlpatterns = [

    url(r'^companies/', include(company_patterns, namespace='companies')),
    url(r'^families/', include(family_patterns, namespace='families')),

]
