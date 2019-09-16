from django.conf.urls import url,include
from . import views
from .views import company
from .views import family


company_patterns =[

    url(r'^create/$',views.company.Create.as_view(),name='create'),
    url(r'^edit/(?P<slug>[-\w]+)/$',views.company.Update.as_view(),name='update'),
    url(r'^(?P<slug>[-\w]+)/$',views.company.Detail.as_view(),name='detail'),

]

urlpatterns = [

    url(r'^company/', include(company_patterns,namespace='companies')),

]