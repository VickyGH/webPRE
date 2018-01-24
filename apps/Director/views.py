from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from apps.Admin.models import Escuelas
from apps.Admin.views import Inicio

from .models import *

# Create your views here.

class InicioSesion(FormView):
    # Establecemos la plantilla a utilizar
    template_name = 'Admin/InicioSesion.html'
    # Le indicamos que el formulario a utilizar es el formulario de autenticación de Django
    form_class = AuthenticationForm
    # Le decimos que cuando se haya completado exitosamente la operación nos redireccione a la url bienvenida de la aplicación personas
    success_url = reverse_lazy('Direc:Inicio')

    def dispatch(self, request, *args, **kwargs):
        # Si el usuario está autenticado entonces nos direcciona a la url establecida en success_url
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        # Sino lo está entonces nos muestra la plantilla del login simplemente
        else:
            return super(InicioSesion, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(InicioSesion, self).form_valid(form)

def InicioDir(request):
    data_user = get_object_or_404(User, id=request.user.id)

    if data_user.perfil.escuela != None:
        id = data_user.perfil.escuela.id
        data_escuela = get_object_or_404(Escuelas, pk=id)
        data_sispre =   get_object_or_404(Escuelas, pk=data_escuela.sispre.id)
        data_contra =   get_object_or_404(Escuelas, pk=data_escuela.contraloria_s.id)

        return render(request, 'Director/Inicio.html',
                  {'escuela': data_escuela,
                   'sispre': data_sispre,
                   'contraloria':data_contra})
    else :
        return render(request, 'Director/NoData.html')