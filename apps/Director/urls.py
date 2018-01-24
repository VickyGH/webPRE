from django.conf.urls import url, include
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required

from apps.Director import views
from .views import *

app_name='Director'
urlpatterns = [
    url(r'^$', InicioSesion.as_view(), name="InicioSesion"),
    url(r'^Salir/$', logout, name="CerrarSesion", kwargs={'next_page': '/'}),
    url(r'^Inicio/$', login_required(views.InicioDir), name='Inicio'),
    #url(r'^NoData/$', login_required(NoData.InicioDir), name='Inicio'),

]