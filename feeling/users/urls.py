from django.conf.urls import url,include
from . import views

urlpatterns =[
    url(r'^dashboard/$',views.Dashboard.as_view(),name='dashboard'),
    url(r'^logout/$',views.LogoutView.as_view(),name='logout'),
    url(r'^signup/$',views.SignupView.as_view(),name='signup'),
    url(r'^signup/$',views.SignupView.as_view(),name='signup'),
    url(r'^company/create/$',views.CompanyCreate.as_view(),name='company_create'),
    url('^',include('django.contrib.auth.urls'))
]