"""feeling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
from users import urls
from thoughts import urls
from group import urls
from django.conf import settings



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls',namespace='users')),
    url(r'^thoughts/', include('thoughts.urls',namespace='thoughts')),
    url(r'^group/', include('group.urls',namespace='group')),
    url(r'^$', TemplateView.as_view(template_name='index.html'),name='home'),
]

if settings.DEBUG:
    import _decimal
    urlpatterns +=[
        url(r'^__debug__/',include(debug_toolbar.urls)),
    ]
