from django.db import models

comp  = (
    #('1 - A Infraestructura','1 - A Infraestructura'),
    #('2 - B Aut. Gest. Escolar', '2 - B Aut. Gest. Escolar'),
    #('2 - C Eval. de Impacto','2 - C Eval. de Impacto')
    ('2 - Aut. Gest. Escolar', '2 - Aut. Gest. Escolar'),
)

acciones = (
    #('No Aplica','No Aplica'),
    ('Mayor', 'Mayor'),
    ('Menor','Menor'),
)

SN = (
    ('No','No'),
    ('Si','Si'),
)

DT = (
    ('Sin Datos', 'Sin Datos'),
    ('En revisión','En revisión'),
    ('Corregir','Corregir'),
    ('Correcto','Correcto'),
)

DTN = (
    ('No Aplica','No Aplica'),
    ('Sin Datos', 'Sin Datos'),
    ('En revisión','En revisión'),
    ('Corregir','Corregir'),
    ('Correcto','Correcto'),
)

IC = (
    ('Incompleto','Incompleto'),
    ('Completo','Completo'),
)
ICA = (
    ('Incompleto','Incompleto'),
    ('Completo','Completo'),
    ('No Aplica', 'No Aplica')
)

nivelE = (
    ('Indígena','Indígena'),
    ('Preescolar','Preescolar'),
    ('Primaria','Primaria'),
    ('Secundaria','Secundaria'),
)

Municipios = (
    ('Balancán','Balancán'),
    ('Cárdenas', 'Cárdenas'),
    ('Centla', 'Centla'),
    ('Centro', 'Centro'),
    ('Comalcalco', 'Comalcalco'),
    ('Cunduacán', 'Cunduacán'),
    ('Emiliano Zapata', 'Emiliano Zapata'),
    ('Huimanguillo', 'Huimanguillo'),
    ('Jalapa', 'Jalapa'),
    ('Jalpa de Méndez', 'Jalpa de Méndez'),
    ('Jonuta', 'Jonuta'),
    ('Macuspana', 'Macuspana'),
    ('Nacajuca', 'Nacajuca'),
    ('Paraíso', 'Paraíso'),
    ('Tacotalpa', 'Tacotalpa'),
    ('Teapa', 'Teapa'),
    ('Tenosique', 'Tenosique'),
)

sinOb = 'Sin observaciones'
# Create your models here.

class Fechas_Finales (models.Model):
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_seguimiento = models.DateField(blank=True, null=True)
    fecha_cierre = models.DateField(blank=True, null=True)
    fecha_constitucion = models.DateField(blank=True, null=True)
    fecha_seguimientoC = models.DateField(blank=True, null=True)
    fecha_anual = models.DateField(blank=True, null=True)
    actualizacion = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'Actualización de Fecha de Finales - ' + self.fecha_inicio

    def __str__(self):
        return '%s' % (self.fecha_inicio)

    class Meta:
        ordering = ['actualizacion']
        verbose_name_plural = "Fecha de Entregas"

class Documentos(models.Model):
    PDF_acta_mancomunado =  models.FileField(upload_to='Cuadernillo/Inicio/', blank=True, null=True)
    PDF_constancia_cepse = models.FileField(upload_to='Cuadernillo/Inicio/', blank=True, null=True)
    PDF_acta_planeacion = models.FileField(upload_to='Cuadernillo/Inicio/', blank=True, null=True)
    PDF_acuse_prog = models.FileField(upload_to='Cuadernillo/Inicio/', blank=True, null=True)
    PDF_compromiso_inmueble = models.FileField(upload_to='Cuadernillo/Inicio/', blank=True, null=True)
    PDF_compromiso_comunidad = models.FileField(upload_to='Cuadernillo/Inicio/', blank=True, null=True)
    PDF_contrato = models.FileField(upload_to='Cuadernillo/Inicio/', blank=True, null=True)

    PDF_acta_cierre = models.FileField(upload_to='Cuadernillo/Cierre/', blank=True, null=True)
    PDF_acta_entrega = models.FileField(upload_to='Cuadernillo/Cierre/', blank=True, null=True)
    PDF_acta_rendicion = models.FileField(upload_to='Cuadernillo/Cierre/', blank=True, null=True)
    PDF_ficha_reintegro = models.FileField(upload_to='Cuadernillo/Cierre/', blank=True, null=True)
    PDF_form_inventario = models.FileField(upload_to='Cuadernillo/Cierre/', blank=True, null=True)
    PDF_form_transferencia = models.FileField(upload_to='Cuadernillo/Cierre/', blank=True, null=True)
    PDF_registro_gastos = models.FileField(upload_to='Cuadernillo/Cierre/', blank=True, null=True)
    PDF_verificacion_sat = models.FileField(upload_to='Cuadernillo/Cierre/', blank=True, null=True)

class Directores (models.Model):
    nombre = models.CharField(max_length=100)
    a_paterno = models.CharField(max_length=100)
    a_materno = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, default='Sin Numero')

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.a_paterno,self.a_materno)

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = "Directores"

class Constitucion (models.Model):
    # Constitucion
    estatusC = models.CharField(max_length=20, choices=IC, default='Incompleto')
    actaC = models.CharField(max_length=40, choices=DT, default=False)
    acta_CArchivo = models.FileField(upload_to='Contraloria_S/Inicio/', blank=True, null=True)
    acta_CObservacion = models.CharField(max_length=250, blank=True)

    minutaC = models.CharField(max_length=40, choices=DT, default=False)
    minuta_CArchivo = models.FileField(upload_to='Contraloria_S/Inicio/', blank=True, null=True)
    minuta_CObservacion = models.CharField(max_length=250, blank=True)

    listaC = models.CharField(max_length=40, choices=DT, default=False)
    lista_CArchivo = models.FileField(upload_to='Contraloria_S/Inicio/', blank=True, null=True)
    lista_CObservacion = models.CharField(max_length=250, blank=True)

    fotoC = models.CharField(max_length=40, choices=DT, default=False)
    foto_CArchivo = models.FileField(upload_to='Contraloria_S/Inicio/Fotos/', blank=True, null=True)
    foto_CObservacion = models.CharField(max_length=250, blank=True)

    cdC = models.CharField(max_length=10, choices=SN, default='No')
    pdfC = models.FileField(upload_to='Contraloria_S/Inicio/', blank=True, null=True)
    observacionC = models.TextField(default=sinOb)

    def __unicode__(self):
        return 'Actualización de Contraloria Social - Constitución - '+self.estatusC

    def __str__(self):
        return '%s' % (self.estatusC)

    class Meta:
        ordering = ['estatusC']
        verbose_name_plural = "Contraloria Social - Constitución"

class Cedula(models.Model):
    # Seguimiento
    estatusCe = models.CharField(max_length=20, choices=IC, default='Incompleto')
    actaCe = models.CharField(max_length=40, choices=DT, default=False)
    acta_CeArchivo = models.FileField(upload_to='Contraloria_S/Seguimiento/', blank=True, null=True)
    acta_CeObservacion = models.CharField(max_length=250, blank=True)

    minutaCe = models.CharField(max_length=40, choices=DT, default=False)
    minuta_CeArchivo = models.FileField(upload_to='Contraloria_S/Seguimiento/', blank=True, null=True)
    minuta_CeObservacion = models.CharField(max_length=250, blank=True)

    listaCe = models.CharField(max_length=40, choices=DT, default=False)
    lista_CeArchivo = models.FileField(upload_to='Contraloria_S/Seguimiento/', blank=True, null=True)
    lista_CeObservacion = models.CharField(max_length=250, blank=True)

    fotoCe = models.CharField(max_length=40, choices=DT, default=False)
    foto_CeArchivo = models.FileField(upload_to='Contraloria_S/Seguimiento/Fotos/', blank=True, null=True)
    foto_CeObservacion = models.CharField(max_length=250, blank=True)

    cdCe = models.CharField(max_length=10, choices=SN, default='No')
    pdfCe = models.FileField(upload_to='Contraloria_S/Seguimiento/', blank=True, null=True)
    observacionCe = models.TextField(default=sinOb)

    def __unicode__(self):
        return 'Actualización de Contraloria Social - Cedula - '+self.estatusCe

    def __str__(self):
        return '%s' % (self.estatusCe)

    class Meta:
        ordering = ['estatusCe']
        verbose_name_plural = "Contraloria Social - Cedula"


class Anual(models.Model):
    # Anual
    estatusA = models.CharField(max_length=20, choices=IC, default='Incompleto')
    actaA = models.CharField(max_length=40, choices=DT, default=False)
    acta_AArchivo = models.FileField(upload_to='Contraloria_S/Anual/', blank=True, null=True)
    acta_AObservacion = models.CharField(max_length=250, blank=True)

    minutaA = models.CharField(max_length=40, choices=DT, default=False)
    minuta_AArchivo = models.FileField(upload_to='Contraloria_S/Anual/', blank=True, null=True)
    minuta_AObservacion = models.CharField(max_length=250, blank=True)

    listaA = models.CharField(max_length=40, choices=DT, default=False)
    lista_AArchivo = models.FileField(upload_to='Contraloria_S/Anual/', blank=True, null=True)
    lista_AObservacion = models.CharField(max_length=250, blank=True)

    fotoA = models.CharField(max_length=40, choices=DT, default=False)
    foto_AArchivo = models.FileField(upload_to='Contraloria_S/Anual/Fotos/', blank=True, null=True)
    foto_AObservacion = models.CharField(max_length=250, blank=True)

    cdA = models.CharField(max_length=10, choices=SN, default='No')
    pdfA = models.FileField(upload_to='Contraloria_S/Anual/', blank=True, null=True)
    observacionA = models.TextField(default=sinOb)

    def __unicode__(self):
        return 'Actualización de Contraloria Social - Anual - '+self.estatusA

    def __str__(self):
        return '%s' % (self.estatusA)

    class Meta:
        ordering = ['estatusA']
        verbose_name_plural = "Contraloria Social - Anual"

class Contraloria_Social (models.Model):
    constitucion = models.ForeignKey(Constitucion, on_delete=False)
    cedula = models.ForeignKey(Cedula, on_delete=False)
    anual = models.ForeignKey(Anual, on_delete=False)
    actualizacion = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'Actualización de Contraloria Social - '+self.constitucion

    def __str__(self):
        return '%s' % (self.constitucion)

    class Meta:
        ordering = ['actualizacion']
        verbose_name_plural = "Contraloria Social"
#<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->
class InicioS (models.Model):
    estatusInicioS = models.CharField(max_length=20, choices=IC, default='Incompleto')

    compromiso_comunidad = models.CharField(max_length=40, choices=DT, default=False)
    compromiso_cArchivo = models.FileField(upload_to='SiSPRE/Inicio/', blank=True, null=True)
    compromiso_cObservacion = models.CharField(max_length=250, blank=True)

    compromiso_inmueble = models.CharField(max_length=25, choices=DT, default='No Aplica')
    compromiso_iArchivo = models.FileField(upload_to='SiSPRE/Inicio/', blank=True, null=True)
    compromiso_iObservacion = models.CharField(max_length=250, blank=True)

    acta_mancomunado = models.CharField(max_length=40,choices=DT, default=False)
    acta_mArchivo = models.FileField(upload_to='PDF/SiSPRE/Inicio/', blank=True, null=True)
    acta_mObservacion = models.CharField(max_length=250,blank=True)

    registro_asignado = models.CharField(max_length=40, choices=DT, default='No Aplica')
    registro_aArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    registro_aObservacion = models.CharField(max_length=250, blank=True)

    acta_planeacion = models.CharField(max_length=40, choices=DT, default=False)
    acta_pArchivo = models.FileField(upload_to='SiSPRE/Inicio/', blank=True, null=True)
    acta_pObservacion = models.CharField(max_length=250, blank=True)

    acuse_banco = models.CharField(max_length=25, choices=DTN, default='No Aplica')
    acuse_bArchivo = models.FileField(upload_to='SiSPRE/Inicio/', blank=True, null=True)
    acuse_bObservacion = models.CharField(max_length=250,blank=True)

    acuse_prog = models.CharField(max_length=40,choices=DT, default=False)
    acuse_pArchivo = models.FileField(upload_to='SiSPRE/Inicio/', blank=True, null=True)
    acuse_pObservacion = models.CharField(max_length=250,blank=True)

    acuse_prog_anterior = models.CharField(max_length=25, choices=DTN, default='No Aplica')
    acuse_prog_aArchivo = models.FileField(upload_to='SiSPRE/Inicio/', blank=True, null=True)
    acuse_prog_aObservacion = models.CharField(max_length=250,blank=True)

    contrato = models.CharField(max_length=25, choices=DTN, default='No Aplica')
    contratoArchivo = models.FileField(upload_to='SiSPRE/Inicio/', blank=True, null=True)
    contratoObservacion = models.CharField(max_length=250,blank=True)

    ife_cepse = models.CharField(max_length=40,choices=DT, default=False)
    ife_cArchivo = models.FileField(upload_to='SiSPRE/Inicio/', blank=True, null=True)
    ife_cObservacion = models.CharField(max_length=250,blank=True)

    constancia_cepse = models.CharField(max_length=40, choices=DT, default=False)
    constancia_cArchivo = models.FileField(upload_to='SiSPRE/Inicio/', blank=True, null=True)
    constancia_cObservacion = models.CharField(max_length=250, blank=True)

    ife_plantel = models.CharField(max_length=40,choices=DT, default=False)
    ife_pArchivo = models.FileField(upload_to='SiSPRE/Inicio/', blank=True, null=True)
    ife_pObservacion = models.CharField(max_length=250,blank=True)

    comision_director = models.CharField(max_length=40,choices=DT, default=False)
    comision_dArchivo = models.FileField(upload_to='PDF/SiSPRE/Inicio/', blank=True, null=True)
    comision_dObservacion = models.CharField(max_length=250,blank=True)

    observacion = models.TextField(default=sinOb)
    foto_fachada = models.ImageField(upload_to='Fotos/Fotos_Fachada/', default='Fotos/Fotos_Fachada/None/no-img.png',
                                     blank=True)

    def __str__(self):
        return '%s' % (self.estatusInicioS)

    class Meta:
        verbose_name_plural = "SISPRE Inicio"

class SeguimientoS (models.Model):
    estatus = models.CharField(max_length=20, choices=ICA, default='Incompleto')
    acta_seguimiento = models.CharField(max_length=25, choices=DT,default='No')
    acta_sArchivo = models.FileField(upload_to='SiSPRE/Seguimiento/', blank=True, null=True)
    acta_sObservacion = models.CharField(max_length=250,blank=True)

    sup_tecnica = models.CharField(max_length=25, choices=DT, default='No Aplica')
    sup_tArchivo = models.FileField(upload_to='SiSPRE/Seguimiento/', blank=True, null=True)
    sup_tObservacion = models.CharField(max_length=250,blank=True)

    evid_seguimiento = models.CharField(max_length=25, choices=DT,default='No',)
    evid_sArchivo = models.FileField(upload_to='SiSPRE/Seguimiento/', blank=True, null=True)
    evid_sObservacion = models.CharField(max_length=250,blank=True)

    acta_circunstanciada = models.CharField(max_length=25, choices=DT, default='No Aplica')
    acta_cArchivo = models.FileField(upload_to='SiSPRE/Seguimiento/', blank=True, null=True)
    acta_cObservacion = models.CharField(max_length=250,blank=True)

    observacion = models.TextField(default=sinOb)

    def __str__(self):
        return '%s' % (self.estatus)

    class Meta:
        verbose_name_plural = "SISPRE Seguimiento"

class CierreS (models.Model):
    estatusCierreS = models.CharField(max_length=40, choices=IC, default='Incompleto')
    acta_cierre = models.CharField(max_length=40, choices=DT, default=False)
    acta_cArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    acta_cObservacion = models.CharField(max_length=250, blank=True)

    registro_gastos = models.CharField(max_length=40, choices=DT, default='No Aplica')
    registro_gArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    registro_gObservacion = models.CharField(max_length=250, blank=True)

    acta_entrega = models.CharField(max_length=40, choices=DT, default='No Aplica')
    acta_eArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    acta_eObservacion = models.CharField(max_length=250, blank=True)

    acta_rendicion = models.CharField(max_length=40, choices=DT, default=False)
    acta_rArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    acta_rObservacion = models.CharField(max_length=250, blank=True)

    facturas = models.CharField(max_length=40, choices=DT, default='No Aplica')
    facturasArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    facturasObservacion = models.CharField(max_length=250, blank=True)

    ficha_reintegro = models.CharField(max_length=40,choices=DT, default=False)
    ficha_rArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    ficha_rObservacion = models.CharField(max_length=250, blank=True)

    form_inventario = models.CharField(max_length=40, choices=DT, default='No Aplica')
    form_iArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    form_iObservacion = models.CharField(max_length=250, blank=True)

    form_transferencia = models.CharField(max_length=40, choices=DT, default='No Aplica')
    form_tArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    form_tObservacion = models.CharField(max_length=250, blank=True)

    evid_obra_concluida = models.CharField(max_length=40, choices=DT, default='No Aplica')
    evid_obraArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    evid_obraObservacion = models.CharField(max_length=250, blank=True)

    evid_compras = models.CharField(max_length=40,choices=DT, default=False)
    evid_cArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    evid_cObservacion = models.CharField(max_length=250, blank=True)

    verificacion_sat = models.CharField(max_length=40,choices=DT, default=False)
    verificacionArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    verificacionObservacion = models.CharField(max_length=250, blank=True)

    xml = models.CharField(max_length=40,choices=DT, default=False)
    xmlArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    xmlObservacion = models.CharField(max_length=250, blank=True)

    observacionCierre = models.TextField(default=sinOb)

    def __str__(self):
        return '%s' % (self.estatusCierreS)

    class Meta:
        verbose_name_plural = "SISPRE Cierre"

class SISPRE (models.Model):
    inicio = models.ForeignKey(InicioS, on_delete=False)
    #seguimiento = models.ForeignKey(SeguimientoS,on_delete=False)
    cierre = models.ForeignKey(CierreS,on_delete=False)
    pdfCompleto = models.FileField(upload_to='PDF/SiSPRE/', blank=True, null=True)
    actualizacion = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'Actualización de SiSPRE - '+self.inicio

    def __str__(self):
        return '%s' % (self.inicio)

    class Meta:
        ordering = ['actualizacion']
        verbose_name_plural = "SiSPRE"

class Escuelas (models.Model):
    cct = models.CharField(max_length=11, verbose_name='C.C.T', )
    nombre = models.CharField(max_length=250, verbose_name='Nombre de la Escuela')
    nivel = models.CharField(max_length=50, choices=nivelE,verbose_name='Nivel Educativo')
    componente = models.CharField(max_length=50, choices=comp, default='2 - Aut. Gest. Escolar', verbose_name='Componente')
    accion = models.CharField(max_length=25,choices=acciones, default='Menor',verbose_name='Accion')
    cambio_accion = models.CharField(max_length=25, default='No', choices=SN, verbose_name='Cambio de Acción')
    ciclo_esc = models.CharField(max_length=100,default="2017-2018")
    municipio = models.CharField(max_length=50,choices=Municipios)
    localidad = models.CharField(max_length=250)
    director = models.ForeignKey(Directores, on_delete=False)
    monto_asignado = models.FloatField()
    monto_ejercido = models.FloatField(default=0)
    monto_restante = models.FloatField(default=0)
    observacion = models.TextField(default=sinOb)
    sispre = models.ForeignKey(SISPRE,on_delete=False)
    contraloria_s = models.ForeignKey(Contraloria_Social,on_delete=False)
    creacion = models.DateTimeField(auto_now=True)
    actualizacion = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.cct +' - '+self.nombre

    def __str__(self):
        return '%s - %s' % (self.cct, self.nombre)

    def save(self, force_insert=False, force_update=False):
        self.cct = self.cct.upper()
        super(Escuelas, self).save(force_insert, force_update)

    class Meta:
        ordering = ['cct']
        verbose_name_plural = "Escuelas"

class Supervisores (models.Model):
    cct = models.CharField(max_length=11)
    nombre = models.CharField(max_length=100)
    a_paterno = models.CharField(max_length=100)
    a_materno = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    zona_escolar = models.IntegerField()
    escuelas_zona = models.ManyToManyField(Escuelas)

    def __unicode__(self):
        return self.cct

    def __str__(self):
        return '%s - %s %s %s' % (self.cct,self.nombre, self.a_paterno,self.a_materno)

    class Meta:
        ordering = ['cct']
        verbose_name_plural = "Supervisores"


from django.db import models
from django.contrib.auth.models import AbstractUser

#class Usuarios(AbstractUser):
#    escuela = models.ForeignKey(Escuelas,null=True)
#    director = models.ForeignKey(Directores, null=True)


from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin = models.CharField(max_length=25, choices=SN,default='No')
    escuela = models.ForeignKey(Escuelas, blank=True,null=True,on_delete=False)
    director = models.ForeignKey(Directores, blank=True,null=True,on_delete=False)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    instance.perfil.save()
