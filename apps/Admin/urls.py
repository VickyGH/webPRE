from django.conf.urls import url, include
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required

from .views import *


urlpatterns = [
    url(r'^$', InicioS_Admin.as_view(), name="InicioSesion"),
    url(r'^Salir/$', logout, name="CerrarSesion", kwargs={'next_page': '/Admin'}),
    url(r'^Inicio/$', login_required(Inicio.as_view()), name='Inicio'),
    #>-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<
    url(r'^Detalles/(?P<pk>\d+)$', login_required(Detalles.as_view()), name='Detalles'),
    url(r'^General/(?P<pk>\d+)$', login_required(General.as_view()), name='General'),
    url(r'^SiSPRE/(?P<pk>\d+)$', login_required(Sispre.as_view()), name='SiSPRE'),
]