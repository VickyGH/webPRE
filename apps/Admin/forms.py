from __future__ import unicode_literals

from django import forms

from django.forms import Textarea, TextInput, Select, FileInput, RadioSelect, CheckboxInput, BooleanField

from .models import Escuelas, SISPRE

class EscuelasForm(forms.ModelForm):
    class Meta:
        model = Escuelas
        fields = '__all__'
        widgets = {
            'cct': TextInput(attrs={'class': 'span8', 'placeholder': "Clave de Centro de Trabajo"}),
            'nombre': TextInput(attrs={'class': 'span8', 'placeholder': "Nombre del Centro de Trabajo"}),
            'nivel': Select(attrs={'class': 'span8', 'placeholder': "Nivel Educativo"}),
            'componente': Select(attrs={'class': 'span8', 'placeholder': 'Componente Beneficiado'}),
            'accion': Select(attrs={'class': 'span8', 'placeholder': 'Tipo de Acción'}),
            'cambio_comp': Select(attrs={'class': 'span3', 'placeholder': 'Cambios Comp.'}),
            'ciclo_esc': TextInput(attrs={'class': 'span8', 'placeholder': 'Ciclo Escolar'}),
            'municipio': Select(attrs={'class': 'span8', 'placeholder': 'Municipio'}),
            'localidad': TextInput(attrs={'class': 'span8', 'placeholder': 'Localidad'}),
            'monto_asignado': TextInput(attrs={'class': 'span8',
                                               'placeholder': 'Monto Asignado',
                                               'id':'monto_asignado',
                                               'onchange':'resulta()'}),
            'monto_ejercido': TextInput(attrs={'class': 'span8',
                                               'placeholder': 'Monto Ejercido',
                                               'id':'monto_ejercido',
                                               'onchange': 'resulta()'}),
            'monto_restante': TextInput(attrs={'class': 'span8',
                                               'placeholder': 'Monto Restante',
                                               'id': 'monto_restante',
                                               'onchange': 'resulta()'}),
            'observacion': Textarea(attrs={'class': 'span8', 'placeholder': 'Observaciones'}),
            'director': Select(attrs={'class': 'span8'}),
            'sispre': Select(attrs={'class': 'span8'}),
            'contraloria_s': Select(attrs={'class': 'span8'})
        }

class SispreForm (forms.ModelForm):
    class Meta:
        model = SISPRE
        fields = '__all__'
        labels = {
            'estatus': 'Estatus',
            'acta_mancomunado' : 'Acta de acuerdo para el ejercicio mancomunado de los recursos',
            'constancia_cepse' : '',
            'acta_planeacion': '',
            'acuse_banco': '',
            'acuse_prog': '',
            'acuse_prog_anterior': '',
            'carta_compromiso_inmueble': '',
            'carta_compromiso_comunidad': '',
            'contrato': '',
            'ife_cepse': '',
            'ife_plantel': '',
            'foto_plantel': '',
            'orden_comision_director': '',
            'acta_seguimiento': '',
            'sup_tecnica': '',
            'evid_seguimiento': '',
            'acta_circunstanciada': '',
            'acta_cierre': '',
            'acta_er_contratista': '',
            'acta_rendicion': '',
            'facturas': '',
            'ficha_reintegro': '',
            'form_inventario': '',
            'form_transferencia': '',
            'evid_obra_concluida': '',
            'evid_compras': '',
            'registro_gastos': '',
            'resumen_gastos': '',
            'verificacion_sat': '',
            'xml': '',
            'pdf': '',
            'observacion': ''
        }
        widgets = {
            'estatus' : TextInput(attrs={'':''}),
            'acta_mancomunado' : CheckboxInput(),
            'constancia_cepse' : CheckboxInput(),
            'acta_planeacion' : CheckboxInput(),
            'acuse_banco' : TextInput(),
            'acuse_prog' : CheckboxInput(),
            'acuse_prog_anterior' : TextInput(),
            'carta_compromiso_inmueble' : TextInput(),
            'carta_compromiso_comunidad' : CheckboxInput(),
            'contrato' : TextInput(),
            'ife_cepse' : CheckboxInput(),
            'ife_plantel' : CheckboxInput(),
            'foto_plantel' : CheckboxInput(),
            'orden_comision_director' : CheckboxInput(),
            'acta_seguimiento' : CheckboxInput(),
            'sup_tecnica' : TextInput(),
            'evid_seguimiento' : CheckboxInput(),
            'acta_circunstanciada' : TextInput(),
            'acta_cierre' : CheckboxInput(),
            'acta_er_contratista' : TextInput(),
            'acta_rendicion' : CheckboxInput(),
            'facturas' : TextInput(),
            'ficha_reintegro' : CheckboxInput(),
            'form_inventario' : TextInput(),
            'form_transferencia' : TextInput(),
            'evid_obra_concluida' : TextInput(),
            'evid_compras' : CheckboxInput(),
            'registro_gastos' : TextInput(),
            'resumen_gastos' : TextInput(),
            'verificacion_sat' : CheckboxInput(),
            'xml' : CheckboxInput(),
            #'pfd' : models.FileField(),
            'observacion' : TextInput()
        }