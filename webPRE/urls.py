"""webPRE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path#, include
from django.conf.urls import include

from django.conf import settings
from django.conf.urls.static import static

#include((pattern_list, app_namespace), namespace=None)
from apps.Admin import views

urlpatterns = [
    path('Serendipia/', admin.site.urls),
    path('Admin/', include('apps.Admin.urls', namespace="Admin")),
    path('Director/', include('apps.Director.urls', namespace='Director')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'apps.Admin.views.error_404'
handler500 = views.error_500