from django.conf.urls import url, include
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required

from apps.Director import views
from apps.Director.forms import MyAuthenticationForm
from .views import *

app_name='Director'
urlpatterns = [
    url(r'^$', InicioSesionDir.as_view(),{'authentication_form':MyAuthenticationForm}, name="InicioSesion"),
#(r'^login/?$','django.contrib.auth.views.login',{'template_name':'login.html', 'authentication_form':MyAuthenticationForm}),

    url(r'^Salir/$', logout, name="CerrarSesion", kwargs={'next_page': '/Director'}),
    url(r'^Inicio/$', login_required(views.InicioDir), name='InicioD'),
    #url(r'^NoData/$', login_required(NoData.InicioDir), name='Inicio'),
    url(r'Edicion//(?P<pk>\d+)$', login_required(Edit_Inicio.as_view()), name='Edit-Inicio'),

]