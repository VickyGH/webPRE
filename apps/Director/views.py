from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from apps.Admin.models import Escuelas, SISPRE, InicioS, SeguimientoS, CierreS, Contraloria_Social, Constitucion, \
    Cedula, Anual


# Create your views here.

class InicioSesionDir(FormView):
    # Establecemos la plantilla a utilizar
    template_name = 'Admin/InicioSesion.html'
    # Le indicamos que el formulario a utilizar es el formulario de autenticación de Django
    form_class = AuthenticationForm
    # Le decimos que cuando se haya completado exitosamente la operación nos redireccione a la url bienvenida de la aplicación personas
    success_url = reverse_lazy('Director:InicioD')

    def dispatch(self, request, *args, **kwargs):
        # Si el usuario está autenticado entonces nos direcciona a la url establecida en success_url
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        # Sino lo está entonces nos muestra la plantilla del login simplemente
        else:
            return super(InicioSesionDir, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(InicioSesionDir, self).form_valid(form)

def InicioDir(request):
    data_user = get_object_or_404(User, id=request.user.id)

    if data_user.perfil.escuela != None:
        id = data_user.perfil.escuela.id
        data_escuela = get_object_or_404(Escuelas, pk=id)
        data_sispre =   get_object_or_404(SISPRE, pk=data_escuela.sispre.id)
        data_contra =   get_object_or_404(Contraloria_Social, pk=data_escuela.contraloria_s.id)

        inicio = get_object_or_404(InicioS, pk=data_sispre.inicio.id)
        #seguimiento = get_object_or_404(SeguimientoS, pk=data_sispre.seguimiento.id)
        cierre = get_object_or_404(CierreS, pk=data_sispre.cierre.id)

        const = get_object_or_404(Constitucion, pk=data_contra.constitucion.id)
        cedula = get_object_or_404(Cedula, pk=data_contra.cedula.id)
        anual = get_object_or_404(Anual, pk=data_contra.anual.id)

        return render(request, 'Director/Inicio.html',
                  {'escuela': data_escuela,
                   'inicio':inicio,
                   #'seguimiento': seguimiento,
                   'cierre': cierre,
                   'const':const,
                   'cedula':cedula,
                   'anual':anual})
    else :
        return render(request, 'Director/NoData.html')