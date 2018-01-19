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

from apps.Admin.forms import EscuelasForm, SispreForm, InicioSForm
from .models import *
from django.contrib.auth.models import User

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

class Sispre1 (UpdateView):
    form_class = SispreForm
    model = SISPRE
    template_name = 'Admin/SiSPRE.html'
    success_url = reverse_lazy('Admin:Inicio')

def Sispre (request,pk_escuela):
    data_escuela = get_object_or_404(Escuelas,id=pk_escuela)
    data_sispre = get_object_or_404(SISPRE, id=data_escuela.sispre.id)
    if request.method == "POST":
        #form = SispreForm(data = request.POST, instance=data_sispre)
        formIni = SispreForm(data=request.POST, instance=data_sispre.inicio.id)
        #formSeg = SispreForm(data=request.POST, instance=data_sispre.seguimiento.id)
        #formCie = SispreForm(data=request.POST, instance=data_sispre.cierre.id)
        if formIni.is_valid(): #& formIni.is_valid() & formSeg.is_valid() & formCie.is_valid():
            #update= form.save()
            update1=formIni.save()
            #update2 = formSeg.save()
            #update3 = formCie.save()
            return reverse_lazy('Admin:Inicio')
        else:
            print('Error')
    else:
        #form = SispreForm(instance=SISPRE.objects.get(id=data_escuela.sispre.id))
        formIni = InicioSForm(instance=InicioS.objects.get(id=data_sispre.inicio.id))
        #formSeg = SispreForm(instance=SeguimientoS.objects.get(id=data_sispre.seguimiento.id))
        #formCie = SispreForm(instance=CierreS.objects.get(id=data_sispre.cierre.id))

    return render_to_response(
        'Admin/SiSPRE.html',
        {
            #'form':form,
            'formI': formIni,
            #'formS': formSeg,
            #'formC': formCie,
            'escuela':data_escuela,
            'sispre':data_sispre
        })



