from __future__ import unicode_literals

from django import forms

from django.forms import Textarea, TextInput, Select, FileInput, RadioSelect, CheckboxInput, BooleanField

from .models import Escuelas, SISPRE, InicioS

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
            'inicio': 'Estatus de Inicio',
            'seguimiento' : 'Estatus de Seguimiento',
            'cierre' : 'Estatus de Cierre',
            'pdfCompleto': 'Archivo de PDF',
        }

class InicioSForm (forms.ModelForm):
    class Meta:
        model = InicioS
        fields = '__all__'
        labels = {
            'estatus': 'Estatus de Inicio',

            'acta_mancomunado' : 'Estatus del Acta de Acuerdo Mancomunado',
            'acta_mArchivo' : 'Archivo de Acta de Acuerdo Mancomunado',
            'acta_mObservacion': 'Observaciones',

            'constancia_cepse': 'Estatus de Constancia de CEPSE',
            'constancia_cArchivo': 'Archivo de Constancia de CEPSE',
            'constancia_cObservacion': 'Observaciones',

            'acta_planeacion': 'Estatus de Acta de Planeación',
            'acta_pArchivo': 'Archivo',
            'acta_pObservacion': 'Observaciones',

            'acuse_banco': 'Estatus de Acuse de Banco',
            'acuse_bArchivo': 'Archivo de Acuse de Banco',
            'acuse_bObservacion': 'Observaciones',

            'acuse_prog': 'Estatus del Acuse del Programa',
            'acuse_pArchivo': 'Archivo del Acuse del Programa',
            'acuse_pObservacion': 'Observaciones',

            'acuse_prog_anterior': 'Estatus de Acuse del Programa del Ciclo Anterior',
            'acuse_prog_aArchivo': 'Archivo de Acuse del Programa del Ciclo Anterior',
            'acuse_prog_aObservacion': 'Observaciones',

            'compromiso_inmueble': 'Estatus del Acta de Compromiso de Inmueble',
            'compromiso_iArchivo': 'Archivo del Acta de Compromiso de Inmueble',
            'compromiso_iObservacion': 'Observaciones',

            'compromiso_comunidad': 'Estatus del Carta de Compromiso de la Comunidad Escolar',
            'compromiso_cArchivo': 'Archivo del Carta de Compromiso de la Comunidad Escolar',
            'compromiso_cObservacion': 'Observaciones',

            'contrato': 'Estado de Documento de Contrato',
            'contratoArchivo': 'Archivo de Documento de Contrato',
            'contratoObservacion': 'Observaciones',

            'ife_cepse': 'Estado de Copia del INE del CEPSE',
            'ife_cArchivo': 'Archivo Copia del INE del CEPSE',
            'ife_cObservacion': 'Observaciones',

            'ife_plantel': 'Estado de Copia del INE del Director',
            'ife_pArchivo': 'Archivo Copia del INE del Director',
            'ife_pObservacion': 'Observaciones',

            'comision_director': 'Estado de Acta de Comisión del Director',
            'comision_dArchivo': 'Archivo de Acta de Comisión del Director',
            'comision_dObservacion': 'Observaciones',

            'observacion': 'Observaciones Generales',
            'foto_fachada': 'Fotografia de la Fachada de la Comunidad Escolar ',
        }