from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('registration.backends.simple.urls')),
]

