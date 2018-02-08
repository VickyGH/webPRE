from __future__ import unicode_literals

from django import forms

from django.forms import Textarea, TextInput, Select, FileInput, RadioSelect, CheckboxInput, BooleanField

from .models import Escuelas, SISPRE, Contraloria_Social, InicioS, SeguimientoS, CierreS, Fechas_Finales, Constitucion, \
    Cedula, Anual

attrEstatus = {'class': 'span3'}
attrSelec = {'class': 'span12'}
attrObj = {'class': 'span12', 'placeholder': 'Observaciones', 'style': 'height: 4em;'}
attrArchivo = {'class': 'span12'}


class Fechas_FinalesForm(forms.ModelForm):
    class Meta:
        model = Fechas_Finales
        fields = '__all__'
        labels = {
            'fecha_inicio': 'Fecha de Entrega de la Documentación de Inicio en la Coordinación del PRE:',
            'fecha_seguimiento': 'Fecha de Entrega de la Documentación del Seguimiento en la Coordinación del PRE:',
            'fecha_cierre': 'Fecha de Entrega de la Documentación de Cierre en la Coordinación del PRE:',
            'fecha_constitucion': 'Fecha de Entrega de la Documentación de Constitución en la Coordinación del PRE:',
            'fecha_seguimientoC': 'Fecha de Entrega de la Documentación del Seguimiento en la Coordinación del PRE:',
            'fecha_anual': 'Fecha de Entrega de la Documentación Anual en la Coordinación del PRE:'
        }


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
            'cambio_accion': Select(attrs={'class': 'span3', 'placeholder': 'Cambio de Acción'}),
            'ciclo_esc': TextInput(attrs={'class': 'span8', 'placeholder': 'Ciclo Escolar'}),
            'municipio': Select(attrs={'class': 'span8', 'placeholder': 'Municipio'}),
            'localidad': TextInput(attrs={'class': 'span8', 'placeholder': 'Localidad'}),
            'monto_asignado': TextInput(attrs={'class': 'span8',
                                               'placeholder': 'Monto Asignado',
                                               'id': 'monto_asignado',
                                               'onchange': 'resulta()'}),
            'monto_ejercido': TextInput(attrs={'class': 'span8',
                                               'placeholder': 'Monto Ejercido',
                                               'id': 'monto_ejercido',
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

        def clean_name(self):
            return self.cleaned_data["cct"].upper()


class SispreForm(forms.ModelForm):
    class Meta:
        model = SISPRE
        fields = '__all__'
        labels = {
            'inicio': 'Estatus de Inicio',
            'seguimiento': 'Estatus de Seguimiento',
            'cierre': 'Estatus de Cierre',
            'fecha_inicio': 'Fecha de Inicio',
            'fecha_seguimiento': 'Fecha de Seguimiento',
            'fecha_cierre': 'Fecha de Cierre',
            'pdfCompleto': 'Archivo de PDF',
        }


class InicioSForm(forms.ModelForm):
    class Meta:
        model = InicioS
        fields = '__all__'
        labels = {
            'estatus': 'Estatus de Inicio',
            'compromiso_comunidad': 'Carta de Compromiso de la Comunidad Escolar',
            'compromiso_cArchivo': 'Archivo del Carta de Compromiso de la Comunidad Escolar',
            'compromiso_cObservacion': 'Observaciones',

            'compromiso_inmueble': 'Acta de Compromiso de Inmueble',
            'compromiso_iArchivo': 'Archivo del Acta de Compromiso de Inmueble',
            'compromiso_iObservacion': 'Observaciones',

            'acta_mancomunado': 'Acta de Acuerdo Mancomunado',
            'acta_mArchivo': 'Archivo de Acta de Acuerdo Mancomunado',
            'acta_mObservacion': 'Observaciones',

            'registro_asignado': 'Registro Monto Asignado',
            'registro_aArchivo': '',
            'registro_aObservacion': '',

            'acta_planeacion': 'Acta de Planeación',
            'acta_pArchivo': 'Archivo',
            'acta_pObservacion': 'Observaciones',

            'acuse_banco': 'Acuse de Tarjeta Bancaria',
            'acuse_bArchivo': 'Archivo de Acuse de Banco',
            'acuse_bObservacion': 'Observaciones',

            'acuse_prog': 'Acuse del Programa',
            'acuse_pArchivo': 'Archivo del Acuse del Programa',
            'acuse_pObservacion': 'Observaciones',

            'acuse_prog_anterior': 'Acuse del Programa del Ciclo Anterior',
            'acuse_prog_aArchivo': 'Archivo de Acuse del Programa del Ciclo Anterior',
            'acuse_prog_aObservacion': 'Observaciones',

            'contrato': 'Documento de Contrato',
            'contratoArchivo': 'Archivo de Documento de Contrato',
            'contratoObservacion': 'Observaciones',

            'ife_cepse': 'Copia del INE del CEPSE',
            'ife_cArchivo': 'Archivo Copia del INE del CEPSE',
            'ife_cObservacion': 'Observaciones',

            'constancia_cepse': 'Constancia de CEPSE',
            'constancia_cArchivo': 'Archivo de Constancia de CEPSE',
            'constancia_cObservacion': 'Observaciones',

            'ife_plantel': 'Copia del INE del Director',
            'ife_pArchivo': 'Archivo Copia del INE del Director',
            'ife_pObservacion': 'Observaciones',

            'comision_director': 'Acta de Comisión del Director',
            'comision_dArchivo': 'Archivo de Acta de Comisión del Director',
            'comision_dObservacion': 'Observaciones',

            'observacion': 'Observaciones Generales',
            'foto_fachada': 'Fotografia de la Fachada de la Comunidad Escolar ',
        }
        widgets = {
            'estatus': Select(attrs=attrEstatus),

            'compromiso_comunidad': Select(attrs=attrSelec),
            'compromiso_cArchivo': FileInput(attrs=attrArchivo),
            'compromiso_cObservacion': Textarea(attrs=attrObj),

            'compromiso_inmueble': Select(attrs=attrSelec),
            'compromiso_iArchivo': FileInput(attrs=attrArchivo),
            'compromiso_iObservacion': Textarea(attrs=attrObj),

            'acta_mancomunado': Select(attrs=attrSelec),
            'acta_mArchivo': FileInput(attrs=attrArchivo),
            'acta_mObservacion': Textarea(attrs=attrObj),

            'registro_asignado': Select(attrs=attrSelec),
            'registro_aArchivo': FileInput(attrs=attrArchivo),
            'registro_aObservacion': Textarea(attrs=attrObj),

            'acta_planeacion': Select(attrs=attrSelec),
            'acta_pArchivo': FileInput(attrs=attrArchivo),
            'acta_pObservacion': Textarea(attrs=attrObj),

            'acuse_banco': Select(attrs=attrSelec),
            'acuse_bArchivo': FileInput(attrs=attrArchivo),
            'acuse_bObservacion': Textarea(attrs=attrObj),

            'acuse_prog': Select(attrs=attrSelec),
            'acuse_pArchivo': FileInput(attrs=attrArchivo),
            'acuse_pObservacion': Textarea(attrs=attrObj),

            'acuse_prog_anterior': Select(attrs=attrSelec),
            'acuse_prog_aArchivo': FileInput(attrs=attrArchivo),
            'acuse_prog_aObservacion': Textarea(attrs=attrObj),

            'contrato': Select(attrs=attrSelec),
            'contratoArchivo': FileInput(attrs=attrArchivo),
            'contratoObservacion': Textarea(attrs=attrObj),

            'ife_cepse': Select(attrs=attrSelec),
            'ife_cArchivo': FileInput(attrs=attrArchivo),
            'ife_cObservacion': Textarea(attrs=attrObj),

            'constancia_cepse': Select(attrs=attrSelec),
            'constancia_cArchivo': FileInput(attrs=attrArchivo),
            'constancia_cObservacion': Textarea(attrs=attrObj),

            'ife_plantel': Select(attrs=attrSelec),
            'ife_pArchivo': FileInput(attrs=attrArchivo),
            'ife_pObservacion': Textarea(attrs=attrObj),

            'comision_director': Select(attrs=attrSelec),
            'comision_dArchivo': FileInput(attrs=attrArchivo),
            'comision_dObservacion': Textarea(attrs=attrObj),

            'observacion': Textarea(attrs=attrObj),
            'foto_fachada': FileInput(attrs=attrArchivo),
        }


class SeguimientoForm(forms.ModelForm):
    class Meta:
        model = SeguimientoS
        fields = '__all__'
        labels = {
            'estatus': 'Estatus de Seguimiento',
            'acta_seguimiento': 'Acta de Seguimiento',
            'acta_sArchivo': '',
            'acta_sObservacion': '',
            'sup_tecnica': 'Supervición Técnica',
            'sup_tArchivo': '',
            'sup_tObservacion': '',
            'evid_seguimiento': 'Evidencia de Seguimiento',
            'evid_sArchivo': '',
            'evid_sObservacion': '',
            'acta_circunstanciada': 'Acta Circunstanciada',
            'acta_cArchivo': '',
            'acta_cObservacion': '',
            'observacion': 'Observaciones Generales',
        }
        widgets = {
            'estatus': Select(attrs=attrEstatus),
            'acta_seguimiento': Select(attrs=attrSelec),
            'acta_sArchivo': FileInput(attrs=attrArchivo),
            'acta_sObservacion': Textarea(attrs=attrObj),

            'sup_tecnica': Select(attrs=attrSelec),
            'sup_tArchivo': FileInput(attrs=attrArchivo),
            'sup_tObservacion': Textarea(attrs=attrObj),

            'evid_seguimiento': Select(attrs=attrSelec),
            'evid_sArchivo': FileInput(attrs=attrArchivo),
            'evid_sObservacion': Textarea(attrs=attrObj),

            'acta_circunstanciada': Select(attrs=attrSelec),
            'acta_cArchivo': FileInput(attrs=attrArchivo),
            'acta_cObservacion': Textarea(attrs=attrObj),

            'observacion': Textarea(attrs=attrObj),
        }


class CierreForm(forms.ModelForm):
    class Meta:
        model = CierreS
        fields = '__all__'
        labels = {
            'estatusCierreS': 'Estatus de Cierre',

            'acta_cierre': 'Acta de Cierre',
            'acta_cArchivo': '',
            'acta_cObservacion': '',

            'registro_gastos': 'Registro de Gastos',
            'registro_gArchivo': '',
            'registro_gObservacion': '',

            'acta_entrega': 'Acta de Entrega Recepción',
            'acta_eArchivo': '',
            'acta_eObservacion': '',

            'acta_rendicion': 'Acta de Rendición de Cuentas',
            'acta_rArchivo ': '',
            'acta_rObservacion': '',

            'facturas': 'Facturas',
            'facturasArchivo': '',
            'facturasObservacion': '',

            'ficha_reintegro': 'Ficha de Reintegro',
            'ficha_rArchivo': '',
            'ficha_rObservacion': '',

            'form_inventario': 'Formato de Inventario',
            'form_iArchivo': '',
            'form_iObservacion': '',

            'form_transferencia': 'Formato de Transferencia',
            'form_tArchivo': '',
            'form_tObservacion': '',

            'evid_obra_concluida': 'Evidencia de Obra Concluida',
            'evid_obraArchivo': '',
            'evid_obraObservacion': '',

            'evid_compras': 'Evidencias de Compras',
            'evid_cArchivo': '',
            'evid_cObservacion': '',

            'verificacion_sat': 'Verificacin SAT',
            'verificacionArchivo': '',
            'verificacionObservacion': '',

            'xml': 'XML',
            'xmlArchivo': '',
            'xmlObservacion': '',

            'observacionCierre': 'Observaciones Generales'
        }
        widgets = {
            'estatusCierreS': Select(attrs=attrEstatus),

            'acta_cierre': Select(attrs=attrSelec),
            'acta_cArchivo': FileInput(attrs=attrArchivo),
            'acta_cObservacion': Textarea(attrs=attrObj),

            'registro_gastos': Select(attrs=attrSelec),
            'registro_gArchivo': FileInput(attrs=attrArchivo),
            'registro_gObservacion': Textarea(attrs=attrObj),

            'acta_entrega': Select(attrs=attrSelec),
            'acta_eArchivo': FileInput(attrs=attrArchivo),
            'acta_eObservacion': Textarea(attrs=attrObj),

            'acta_rendicion': Select(attrs=attrSelec),
            'acta_rArchivo ': FileInput(attrs=attrArchivo),
            'acta_rObservacion': Textarea(attrs=attrObj),

            'facturas': Select(attrs=attrSelec),
            'facturasArchivo': FileInput(attrs=attrArchivo),
            'facturasObservacion': Textarea(attrs=attrObj),

            'ficha_reintegro': Select(attrs=attrSelec),
            'ficha_rArchivo': FileInput(attrs=attrArchivo),
            'ficha_rObservacion': Textarea(attrs=attrObj),

            'form_inventario': Select(attrs=attrSelec),
            'form_iArchivo': FileInput(attrs=attrArchivo),
            'form_iObservacion': Textarea(attrs=attrObj),

            'form_transferencia': Select(attrs=attrSelec),
            'form_tArchivo': FileInput(attrs=attrArchivo),
            'form_tObservacion': Textarea(attrs=attrObj),

            'evid_obra_concluida': Select(attrs=attrSelec),
            'evid_obraArchivo': FileInput(attrs=attrArchivo),
            'evid_obraObservacion': Textarea(attrs=attrObj),

            'evid_compras': Select(attrs=attrSelec),
            'evid_cArchivo': FileInput(attrs=attrArchivo),
            'evid_cObservacion': Textarea(attrs=attrObj),

            'verificacion_sat': Select(attrs=attrSelec),
            'verificacionArchivo': FileInput(attrs=attrArchivo),
            'verificacionObservacion': Textarea(attrs=attrObj),

            'xml': Select(attrs=attrSelec),
            'xmlArchivo': FileInput(attrs=attrArchivo),
            'xmlObservacion': Textarea(attrs=attrObj),

            'observacionCierre': Textarea(attrs=attrObj)
        }


class ConstitucionForm(forms.ModelForm):
    class Meta:
        model = Constitucion
        fields = '__all__'
        labels = {
            'estatus': 'Estatus Constitución',
            'acta': 'Acta Constitución',
            'acta_Archivo': '',
            'acta_Observacion': '',

            'minuta': 'Minuta',
            'minuta_Archivo': '',
            'minuta_Observacion': '',

            'lista': 'Lista de Asistencia',
            'lista_Archivo': '',
            'lista_Observacion': '',

            'foto': 'Fotografias',
            'foto_Archivo': '',
            'foto_Observacion': '',

            'cd': 'Entrega de CD',
            'pdf': 'PDF Completo',
            'observacion': 'Observaciones'
        }
        widgets = {
            'estatus': Select(attrs=attrEstatus),
            'acta': Select(attrs=attrSelec),
            'acta_Archivo': FileInput(attrs=attrArchivo),
            'acta_Observacion': Textarea(attrs=attrObj),

            'minuta': Select(attrs=attrSelec),
            'minuta_Archivo': FileInput(attrs=attrArchivo),
            'minuta_Observacion': Textarea(attrs=attrObj),

            'lista': Select(attrs=attrSelec),
            'lista_Archivo': FileInput(attrs=attrArchivo),
            'lista_Observacion': Textarea(attrs=attrObj),

            'foto': Select(attrs=attrSelec),
            'foto_Archivo': FileInput(attrs=attrArchivo),
            'foto_Observacion': Textarea(attrs=attrObj),

            'cd': Select(attrs=attrEstatus),
            'pdf': FileInput(attrs=attrArchivo),
            'observacion': Textarea(attrs=attrObj),
        }


class CedulaForm(forms.ModelForm):
    class Meta:
        model = Cedula
        fields = '__all__'
        labels = {
            'estatus': 'Estatus Cedula',
            'acta': 'Acta Cedula',
            'acta_Archivo': '',
            'acta_Observacion': '',

            'minuta': 'Minuta',
            'minuta_Archivo': '',
            'minuta_Observacion': '',

            'lista': 'Lista de Asistencia',
            'lista_Archivo': '',
            'lista_Observacion': '',

            'foto': 'Fotografias',
            'foto_Archivo': '',
            'foto_Observacion': '',

            'cd': 'Entrega de CD',
            'pdf': 'PDF Completo',
            'observacion': 'Observaciones'
        }
        widgets = {
            'estatus': Select(attrs=attrEstatus),
            'acta': Select(attrs=attrSelec),
            'acta_Archivo': FileInput(attrs=attrArchivo),
            'acta_Observacion': Textarea(attrs=attrObj),

            'minuta': Select(attrs=attrSelec),
            'minuta_Archivo': FileInput(attrs=attrArchivo),
            'minuta_Observacion': Textarea(attrs=attrObj),

            'lista': Select(attrs=attrSelec),
            'lista_Archivo': FileInput(attrs=attrArchivo),
            'lista_Observacion': Textarea(attrs=attrObj),

            'foto': Select(attrs=attrSelec),
            'foto_Archivo': FileInput(attrs=attrArchivo),
            'foto_Observacion': Textarea(attrs=attrObj),

            'cd': Select(attrs=attrEstatus),
            'pdf': FileInput(attrs=attrArchivo),
            'observacion': Textarea(attrs=attrObj),
        }


class AnualForm(forms.ModelForm):
    class Meta:
        model = Anual
        fields = '__all__'
        labels = {
            'estatus': 'Estatus Anual',
            'acta': 'Acta Anual',
            'acta_Archivo': '',
            'acta_Observacion': '',

            'minuta': 'Minuta',
            'minuta_Archivo': '',
            'minuta_Observacion': '',

            'lista': 'Lista de Asistencia',
            'lista_Archivo': '',
            'lista_Observacion': '',

            'foto': 'Fotografias',
            'foto_Archivo': '',
            'foto_Observacion': '',

            'cd': 'Entrega de CD',
            'pdf': 'PDF Completo',
            'observacion': 'Observaciones'
        }
        widgets = {
            'estatus': Select(attrs=attrEstatus),
            'acta': Select(attrs=attrSelec),
            'acta_Archivo': FileInput(attrs=attrArchivo),
            'acta_Observacion': Textarea(attrs=attrObj),

            'minuta': Select(attrs=attrSelec),
            'minuta_Archivo': FileInput(attrs=attrArchivo),
            'minuta_Observacion': Textarea(attrs=attrObj),

            'lista': Select(attrs=attrSelec),
            'lista_Archivo': FileInput(attrs=attrArchivo),
            'lista_Observacion': Textarea(attrs=attrObj),

            'foto': Select(attrs=attrSelec),
            'foto_Archivo': FileInput(attrs=attrArchivo),
            'foto_Observacion': Textarea(attrs=attrObj),

            'cd': Select(attrs=attrEstatus),
            'pdf': FileInput(attrs=attrArchivo),
            'observacion': Textarea(attrs=attrObj),
        }


# class ContraloriaForm(forms.ModelForm):
#     class Meta:
#         model = Contraloria_Social
#         fields = '__all__'
#         labels = {
#             'estatus': 'Estatus General',
#
#             'estatusC': 'Estatus de Acta Constitución',
#             'acta_constitucion': 'Acta Constitución',
#             'acta_cArchivo': '',
#             'acta_cObservacion': '',
#
#             'minuta_constitucion': 'Minuta',
#             'minuta_cArchivo': '',
#             'minuta_cObservacion': '',
#
#             'lista_constitucion': 'Lista de Asistencia',
#             'lista_cArchivo': '',
#             'lista_cObservacion': '',
#
#             'foto_constitucion': 'Fotografia de la Reunión',
#             'foto_cArchivo': '',
#             'foto_cObservacion': '',
#
#             'cd_constitucion': 'Entrega de CD',
#             'pdf_constitucion': 'PDF del Rubro',
#
#             'estatusS': 'Estatus de Acta de Seguimiento',
#             'acta_seguimiento': 'Acta de Seguimiento',
#             'acta_sArchivo': '',
#             'acta_sObservacion': '',
#
#             'minuta_seguimiento': 'Minuta',
#             'minuta_sArchivo': '',
#             'minuta_sObservacion': '',
#
#             'lista_seguimiento': 'Lista de Asistencia',
#             'lista_sArchivo': '',
#             'lista_sObservacion': '',
#
#             'foto_seguimiento': 'Fotografia de Reunión',
#             'foto_sArchivo': '',
#             'foto_sObservacion': '',
#
#             'cd_seguimiento': 'Entrega de CD',
#             'pdf_seguimiento': 'PDF del Rubro',
#
#             'estatusA': 'Estatus de Acta Anual',
#             'acta_anual': 'Acta Anual',
#             'acta_aArchivo': '',
#             'acta_aObservacion': '',
#
#             'minuta_anual': 'Minuta',
#             'minuta_aArchivo': '',
#             'minuta_aObservacion': '',
#
#             'lista_anual': 'Lista de Asistencia',
#             'lista_aArchivo': '',
#             'lista_aObservacion': '',
#
#             'foto_anual': 'Fotografia de la Reunión',
#             'foto_aArchivo': '',
#             'foto_aObservacion': '',
#
#             'cd_anual': 'Entrega de CD',
#             'pdf_anual': 'PDF del Rubro',
#
#             'observacion': 'Observaciones Generales',
#             'actualizacion': ''
#         }
#         widgets = {
#             'estatusC': Select(attrs=attrEstatus),
#             'acta_constitucion': Select(attrs=attrSelec),
#             'acta_cArchivo': FileInput(attrs=attrArchivo),
#             'acta_cObservacion': Textarea(attrs=attrObj),
#
#             'minuta_constitucion': Select(attrs=attrSelec),
#             'minuta_cArchivo': FileInput(attrs=attrArchivo),
#             'minuta_cObservacion': Textarea(attrs=attrObj),
#
#             'lista_constitucion': Select(attrs=attrSelec),
#             'lista_cArchivo': FileInput(attrs=attrArchivo),
#             'lista_cObservacion': Textarea(attrs=attrObj),
#
#             'foto_constitucion': Select(attrs=attrSelec),
#             'foto_cArchivo': FileInput(attrs=attrArchivo),
#             'foto_cObservacion': Textarea(attrs=attrObj),
#
#             'cd_constitucion': Select(attrs=attrEstatus),
#             'pdf_constitucion': FileInput(attrs=attrArchivo),
#
#             'estatusS': Select(attrs=attrEstatus),
#             'acta_seguimiento': Select(attrs=attrSelec),
#             'acta_sArchivo': FileInput(attrs=attrArchivo),
#             'acta_sObservacion': Textarea(attrs=attrObj),
#
#             'minuta_seguimiento': Select(attrs=attrSelec),
#             'minuta_sArchivo': FileInput(attrs=attrArchivo),
#             'minuta_sObservacion': Textarea(attrs=attrObj),
#
#             'lista_seguimiento': Select(attrs=attrSelec),
#             'lista_sArchivo': FileInput(attrs=attrArchivo),
#             'lista_sObservacion': Textarea(attrs=attrObj),
#
#             'foto_seguimiento': Select(attrs=attrSelec),
#             'foto_sArchivo': FileInput(attrs=attrArchivo),
#             'foto_sObservacion': Textarea(attrs=attrObj),
#
#             'cd_seguimiento': Select(attrs=attrEstatus),
#             'pdf_seguimiento': FileInput(attrs=attrArchivo),
#
#             'estatusA': Select(attrs=attrEstatus),
#             'acta_anual': Select(attrs=attrSelec),
#             'acta_aArchivo': FileInput(attrs=attrArchivo),
#             'acta_aObservacion': Textarea(attrs=attrObj),
#
#             'minuta_anual': Select(attrs=attrSelec),
#             'minuta_aArchivo': FileInput(attrs=attrArchivo),
#             'minuta_aObservacion': Textarea(attrs=attrObj),
#
#             'lista_anual': Select(attrs=attrSelec),
#             'lista_aArchivo': FileInput(attrs=attrArchivo),
#             'lista_aObservacion': Textarea(attrs=attrObj),
#
#             'foto_anual': Select(attrs=attrSelec),
#             'foto_aArchivo': FileInput(attrs=attrArchivo),
#             'foto_aObservacion': Textarea(attrs=attrObj),
#
#             'cd_anual': Select(attrs=attrEstatus),
#             'pdf_anual': FileInput(attrs=attrArchivo),
#
#             'observacion': Textarea(attrs=attrObj),
#             'actualizacion': ''
#         }
