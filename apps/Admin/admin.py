from django.contrib import admin

from .models import *

# Register your models here.
#from django.contrib.auth.admin import UserAdmin
#admin.site.register(User, UserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Perfil

class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'Perfil'
    fk_name = 'user'
    list = ['admin']

class CustomUserAdmin(UserAdmin):
    inlines = (PerfilInline, )
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

class EscuelaAdmin(admin.ModelAdmin):
    fields = ['cct',
              'nombre',
              'nivel',
              'componente',
              'accion',
              'cambio_comp',
              'director',
              'ciclo_esc',
              'municipio',
              'localidad',
              'monto_asignado',
              'monto_ejercido',
              'sispre'
              #contraloria_s',
              #'observacion'
    ]

class DirectoresAdmin (admin.ModelAdmin):
    fields = ['nombre','a_paterno','a_materno','telefono']

class Contraloria_SocialAdmin (admin.ModelAdmin):
    fields = ['estatus',
              'acta_constitucion',
              'minuta_constitucion',
              'lista_constitucion',
              'foto_constitucion',
              'cd_constitucion',
              'pdf_constitucion',
              'acta_seguimiento',
              'minuta_seguimiento',
              'lista_seguimiento',
              'foto_seguimiento',
              'cd_seguimiento',
              'pdf_seguimiento',
              'acta_anual',
              'minuta_anual',
              'lista_anual',
              'foto_anual',
              'cd_anual',
              'pdf_anual',
              'observacion',
              ]

class InicioSAdmin (admin.ModelAdmin):
    fields = ['estatus',
              'acta_mancomunado',
              'acta_mArchivo',
              'acta_mObservacion',
              'constancia_cepse',
              'constancia_cArchivo',
              'constancia_cObservacion',
              'acta_planeacion',
              'acta_pArchivo',
              'acta_pObservacion',
              'acuse_banco',
              'acuse_bArchivo',
              'acuse_bObservacion',
              'acuse_prog',
              'acuse_pArchivo',
              'acuse_pObservacion',
              'acuse_prog_anterior',
              'acuse_prog_aArchivo',
              'acuse_prog_aObservacion',
              'compromiso_inmueble',
              'compromiso_iArchivo',
              'compromiso_iObservacion',
              'compromiso_comunidad',
              'compromiso_cArchivo',
              'compromiso_cObservacion',
              'contrato',
              'contratoArchivo',
              'contratoObservacion',
              'ife_cepse',
              'ife_cArchivo',
              'ife_cObservacion',
              'ife_plantel',
              'ife_pArchivo',
              'ife_pObservacion',
              'comision_director',
              'comision_dArchivo',
              'comision_dObservacion',
              'observacion',
              'foto_fachada']

class SeguimientoAdmin(admin.ModelAdmin):
    fields = [
        'estatus',
        'acta_seguimiento',
        'acta_sArchivo',
        'acta_sObservacion',
        'sup_tecnica',
        'sup_tArchivo',
        'sup_tObservacion',
        'evid_seguimiento',
        'evid_sArchivo',
        'evid_sObservacion',
        'acta_circunstanciada',
        'acta_cArchivo',
        'acta_cObservacion',
        'observacion',
    ]

class CierreSAdmin(admin.ModelAdmin):
    fields = [
        'estatus',
        'acta_cierre',
        'acta_cArchivo',
        'acta_cObservacion',
        'acta_entrega',
        'acta_eArchivo',
        'acta_eObservacion',
        'acta_rendicion',
        'acta_rArchivo',
        'acta_rObservacion',
        'facturas',
        'facturasArchivo',
        'facturasObservacion',
        'ficha_reintegro',
        'ficha_rArchivo',
        'ficha_rObservacion',
        'form_inventario',
        'form_iArchivo',
        'form_iObservacion',
        'form_transferencia',
        'form_tArchivo',
        'form_tObservacion',
        'evid_obra_concluida',
        'evid_obraArchivo',
        'evid_obraObservacion',
        'evid_compras',
        'evid_cArchivo',
        'evid_cObservacion',
        'registro_gastos',
        'registro_gArchivo',
        'registro_gObservacion',
        'resumen_gastos',
        'resumen_gArchivo',
        'resumen_gObservacion',
        'verificacion_sat',
        'verificacionArchivo',
        'verificacionObservacion',
        'xml',
        'xmlArchivo',
        'xmlObservacion',
        'observacion',
    ]

class SISPREAdmin (admin.ModelAdmin):
    fields = [
        'inicio',
        'seguimiento',
        'cierre',
        'pdfCompleto'
    ]

class SupervisoresAdmin(admin.ModelAdmin):
    fields = ['cct',
              'nombre',
              'a_paterno',
              'a_materno',
              'telefono',
              'zona_escolar',
              'escuelas_zona',
              ]

#admin.site.register(Municipios,MunicipiosAdmin)
admin.site.register(Escuelas,EscuelaAdmin)
admin.site.register(Directores,DirectoresAdmin)
admin.site.register(Contraloria_Social,Contraloria_SocialAdmin)
admin.site.register(SISPRE,SISPREAdmin)
admin.site.register(Supervisores,SupervisoresAdmin)

admin.site.register(InicioS,InicioSAdmin)
admin.site.register(SeguimientoS,SeguimientoAdmin)
admin.site.register(CierreS,CierreSAdmin)













