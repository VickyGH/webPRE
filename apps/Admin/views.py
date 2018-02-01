from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.template.context_processors import request
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

from apps.Admin.forms import EscuelasForm, InicioSForm, SeguimientoForm, CierreForm, ConstitucionForm, CedulaForm, AnualForm
from .models import *

# Create your views here.
def error_404(request):
    data = {}
    return render(request, '404.html', data)

def error_500(request):
    data = {}
    return render(request, '500.html', data)

class InicioS_Admin(FormView):
    # Establecemos la plantilla a utilizar
    template_name = 'Admin/InicioSesion.html'
    # Le indicamos que el formulario a utilizar es el formulario de autenticación de Django
    form_class = AuthenticationForm
    # Le decimos que cuando se haya completado exitosamente la operación nos redireccione a la url bienvenida de la aplicación personas
    success_url = reverse_lazy('Admin:Inicio')

    def dispatch(self, request, *args, **kwargs):
        # Si el usuario está autenticado entonces nos direcciona a la url establecida en success_url
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        # Sino lo está entonces nos muestra la plantilla del login simplemente
        else:
            return super(InicioS_Admin, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(InicioS_Admin, self).form_valid(form)

class Inicio(ListView):
    template_name = 'Admin/Inicio.html'
    model = Escuelas
    paginate_by = 25

class Detalles(DetailView):
    model = Escuelas

class General(UpdateView):
    form_class = EscuelasForm
    model = Escuelas
    template_name = 'Admin/General.html'
    success_url = reverse_lazy('Admin:Inicio')

def Sispre(request, pk):
    data_escuela = get_object_or_404(Escuelas, id=pk)
    data_sispre = get_object_or_404(SISPRE, pk=data_escuela.sispre.id)
    fecha = get_object_or_404(Fechas_Finales, pk=1)

    data_inicio = get_object_or_404(InicioS, pk=data_sispre.inicio.id)
    data_seg = get_object_or_404(SeguimientoS, pk=data_sispre.seguimiento.id)
    data_cierre = get_object_or_404(SeguimientoS, pk=data_sispre.cierre.id)

    if request.method == "POST":
        form = InicioSForm(request.POST, instance=data_inicio)
        formS = SeguimientoForm(request.POST, instance=data_seg)
        formC = CierreForm(request.POST, instance=data_cierre)
        if all([form.is_valid(), formS.is_valid(), formC.is_valid()]):
        #if form.is_valid():
            data_inicio = form.save(commit=False)
            data_inicio.save()
            data_seg = formS.save(commit=False)
            data_seg.save()
            data_cierre = formC.save(commit=False)
            data_cierre.save()
            return redirect('Admin:Inicio')
    else:
        form = InicioSForm(instance=data_inicio)
        formS = SeguimientoForm(instance=data_seg)
        formC = CierreForm(instance = data_cierre)
    return render(request, 'Admin/SiSPRE.html',
                  {'formI': form,
                   'formS':formS,
                   'formC':formC,
                   'escuela':data_escuela,
                   'sispre':data_sispre,
                   'fecha' : fecha})

def ContraloriaS(request, pk):
    data_escuela = get_object_or_404(Escuelas, id=pk)
    data_contraloria = get_object_or_404(Contraloria_Social, pk=data_escuela.contraloria_s.id)
    fecha = get_object_or_404(Fechas_Finales, pk=1)

    data_constitucion = get_object_or_404(Constitucion, pk=data_contraloria.constitucion.id)
    data_seg = get_object_or_404(Cedula, pk=data_contraloria.cedula.id)
    data_cierre = get_object_or_404(Anual, pk=data_contraloria.anual.id)

    if request.method == "POST":
        form = ConstitucionForm(request.POST, instance=data_constitucion)
        formS = CedulaForm(request.POST, instance=data_seg)
        formC = AnualForm(request.POST, instance=data_cierre)
        if all([form.is_valid(), formC.is_valid()]):#, formC.is_valid()]):
        #if form.is_valid():
            data_constitucion = form.save(commit=False)
            data_constitucion.save()
            data_seg = formS.save(commit=False)
            data_seg.save()
            data_cierre = formC.save(commit=False)
            data_cierre.save()
            return redirect('Admin:Inicio')
    else:
        form = ConstitucionForm(instance=data_constitucion)
        formS = CedulaForm(instance=data_seg)
        formC = AnualForm(instance = data_cierre)
    return render(request, 'Admin/ContraloriaS.html',
                  {'formC': form,
                   'formCe':formS,
                   'formA':formC,
                   'escuela':data_escuela,
                   'contraloria':data_contraloria,
                   'fecha' : fecha})