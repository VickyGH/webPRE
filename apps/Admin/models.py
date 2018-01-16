from django.db import models

comp  = (
    ('1 - A INFRAESTRUCTURA', '1 - A INFRAESTRUCTURA'),
    ('2 - B AUT. GEST. ESCOLAR', '2 - B AUT. GEST. ESCOLAR'),
    ('2 - C EVAL. DE IMPACTO','2 - C EVAL. DE IMPACTO')
)

acciones = (
    ('No Aplica','No Aplica'),
    ('Mayor', 'Mayor'),
    ('Menor','Menor'),
)

SN = (
    (False,'No'),
    (True,'Si'),
)

DT = (
    ('Sin Datos', 'Sin Datos'),
    ('En revisión','En revisión'),
    ('Corregir','Corregir'),
    ('Correcto','Correcto'),
)

IC = (
    ('Incompleto','Incompleto'),
    ('Completo','Completo'),
)

nivelE = (
    ('INDÍGENA','INDÍGENA'),
    ('PREESCOLAR','PREESCOLAR'),
    ('PRIMARIA','PRIMARIA'),
    ('SECUNDARIA','SECUNDARIA'),
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
# Create your models here.
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

class Contraloria_Social (models.Model):
    estatus = models.CharField(max_length=20,choices=IC, default='Incompleto')
    acta_constitucion = models.BooleanField(choices=SN, default=False)
    minuta_constitucion = models.BooleanField(choices=SN, default=False)
    lista_constitucion = models.BooleanField(choices=SN, default=False)
    foto_constitucion = models.BooleanField(choices=SN, default=False)
    cd_constitucion = models.BooleanField(choices=SN, default=False)
    pdf_constitucion = models.FileField(upload_to='PDF/Contraloria_S/Inicio/',blank=True, null=True)
    acta_seguimiento = models.BooleanField(choices=SN, default=False)
    minuta_seguimiento = models.BooleanField(choices=SN, default=False)
    lista_seguimiento = models.BooleanField(choices=SN, default=False)
    foto_seguimiento= models.BooleanField(choices=SN, default=False)
    cd_seguimiento = models.BooleanField(choices=SN, default=False)
    pdf_seguimiento = models.FileField(upload_to='PDF/Contraloria_S/Seguimiento/',blank=True, null=True)
    acta_anual = models.BooleanField(choices=SN, default=False)
    minuta_anual  = models.BooleanField(choices=SN, default=False)
    lista_anual = models.BooleanField(choices=SN, default=False)
    foto_anual = models.BooleanField(choices=SN, default=False)
    cd_anual = models.BooleanField(choices=SN, default=False)
    pdf_anual = models.FileField(upload_to='PDF/Contraloria_S/Cierre/',blank=True, null=True)
    observacion = models.TextField(default='Sin observacion')
    actualizacion = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'Actualización de Contraloria Social - '+self.actualizacion

    def __str__(self):
        return '%s' % (self.estatus)

    class Meta:
        ordering = ['actualizacion']
        verbose_name_plural = "Contraloria Social"
#<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->-<->
class InicioS (models.Model):
    estatus = models.CharField(max_length=20, choices=IC, default='Incompleto')

    acta_mancomunado = models.CharField(max_length=40,choices=DT, default=False)
    acta_mArchivo = models.FileField(upload_to='PDF/SiSPRE/Inicio/', blank=True, null=True)
    acta_mObservacion = models.CharField(max_length=250,blank=True)

    constancia_cepse = models.CharField(max_length=40,choices=DT, default=False)
    constancia_cArchivo = models.FileField(upload_to='PDF/SiSPRE/Inicio/', blank=True, null=True)
    constancia_cObservacion = models.CharField(max_length=250,blank=True)

    acta_planeacion = models.CharField(max_length=40,choices=DT, default=False)
    acta_pArchivo = models.FileField(upload_to='PDF/SiSPRE/Inicio/', blank=True, null=True)
    acta_pObservacion = models.CharField(max_length=250,blank=True)

    acuse_banco = models.CharField(max_length=25, choices=acciones, default='No Aplica')
    acuse_bArchivo = models.FileField(upload_to='PDF/SiSPRE/Inicio/', blank=True, null=True)
    acuse_bObservacion = models.CharField(max_length=250,blank=True)

    acuse_prog = models.CharField(max_length=40,choices=DT, default=False)
    acuse_pArchivo = models.FileField(upload_to='PDF/SiSPRE/Inicio/', blank=True, null=True)
    acuse_pObservacion = models.CharField(max_length=250,blank=True)

    acuse_prog_anterior = models.CharField(max_length=25, choices=acciones, default='No Aplica')
    acuse_prog_aArchivo = models.FileField(upload_to='PDF/SiSPRE/Inicio/', blank=True, null=True)
    acuse_prog_aObservacion = models.CharField(max_length=250,blank=True)

    compromiso_inmueble = models.CharField(max_length=25, choices=acciones, default='No Aplica')
    compromiso_iArchivo = models.FileField(upload_to='PDF/SiSPRE/Inicio/', blank=True, null=True)
    compromiso_iObservacion = models.CharField(max_length=250,blank=True)

    compromiso_comunidad = models.CharField(max_length=40,choices=DT, default=False)
    compromiso_cArchivo = models.FileField(upload_to='PDF/SiSPRE/Inicio/', blank=True, null=True)
    compromiso_cObservacion = models.CharField(max_length=250,blank=True)

    contrato = models.CharField(max_length=25, choices=acciones, default='No Aplica')
    contratoArchivo = models.FileField(upload_to='PDF/SiSPRE/Inicio/', blank=True, null=True)
    contratoObservacion = models.CharField(max_length=250,blank=True)

    ife_cepse = models.CharField(max_length=40,choices=DT, default=False)
    ife_cArchivo = models.FileField(upload_to='PDF/SiSPRE/Inicio/', blank=True, null=True)
    ife_cObservacion = models.CharField(max_length=250,blank=True)

    ife_plantel = models.CharField(max_length=40,choices=DT, default=False)
    ife_pArchivo = models.FileField(upload_to='PDF/SiSPRE/Inicio/', blank=True, null=True)
    ife_pObservacion = models.CharField(max_length=250,blank=True)

    comision_director = models.CharField(max_length=40,choices=DT, default=False)
    comision_dArchivo = models.FileField(upload_to='PDF/SiSPRE/Inicio/', blank=True, null=True)
    comision_dObservacion = models.CharField(max_length=250,blank=True)

    observacion = models.TextField(default='Sin observacion')
    foto_fachada = models.ImageField(upload_to='Fotos/Fotos_Fachada/', default='Fotos/Fotos_Fachada/None/no-img.png',
                                     blank=True)

    def __str__(self):
        return '%s' % (self.estatus)

    class Meta:
        verbose_name_plural = "SISPRE Inicio"

class SeguimientoS (models.Model):
    estatus = models.CharField(max_length=20, choices=IC, default='Incompleto')
    acta_seguimiento = models.BooleanField(choices=SN, default=False)
    acta_sArchivo = models.FileField(upload_to='PDF/SiSPRE/Seguimiento/', blank=True, null=True)
    acta_sObservacion = models.CharField(max_length=250,blank=True)

    sup_tecnica = models.CharField(max_length=25, choices=acciones, default='No Aplica')
    sup_tArchivo = models.FileField(upload_to='PDF/SiSPRE/Seguimiento/', blank=True, null=True)
    sup_tObservacion = models.CharField(max_length=250,blank=True)

    evid_seguimiento = models.BooleanField(choices=SN, default=False)
    evid_sArchivo = models.FileField(upload_to='PDF/SiSPRE/Seguimiento/', blank=True, null=True)
    evid_sObservacion = models.CharField(max_length=250,blank=True)

    acta_circunstanciada = models.CharField(max_length=25, choices=acciones, default='No Aplica')
    acta_cArchivo = models.FileField(upload_to='PDF/SiSPRE/Seguimiento/', blank=True, null=True)
    acta_cObservacion = models.CharField(max_length=250,blank=True)

    observacion = models.TextField(default='Sin observacion')

    def __str__(self):
        return '%s' % (self.estatus)

    class Meta:
        verbose_name_plural = "SISPRE Seguimiento"

class CierreS (models.Model):
    estatus = models.CharField(max_length=20, choices=IC, default='Incompleto')
    acta_cierre = models.BooleanField(choices=SN, default=False)
    acta_cArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    acta_cObservacion = models.CharField(max_length=250, blank=True)

    acta_entrega = models.CharField(max_length=25, choices=acciones, default='No Aplica')
    acta_eArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    acta_eObservacion = models.CharField(max_length=250, blank=True)

    acta_rendicion = models.BooleanField(choices=SN, default=False)
    acta_rArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    acta_rObservacion = models.CharField(max_length=250, blank=True)

    facturas = models.CharField(max_length=25, choices=acciones, default='No Aplica')
    facturasArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    facturasObservacion = models.CharField(max_length=250, blank=True)

    ficha_reintegro = models.BooleanField(choices=SN, default=False)
    ficha_rArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    ficha_rObservacion = models.CharField(max_length=250, blank=True)

    form_inventario = models.CharField(max_length=25, choices=acciones, default='No Aplica')
    form_iArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    form_iObservacion = models.CharField(max_length=250, blank=True)

    form_transferencia = models.CharField(max_length=25, choices=acciones, default='No Aplica')
    form_tArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    form_tObservacion = models.CharField(max_length=250, blank=True)

    evid_obra_concluida = models.CharField(max_length=25, choices=acciones, default='No Aplica')
    evid_obraArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    evid_obraObservacion = models.CharField(max_length=250, blank=True)

    evid_compras = models.BooleanField(choices=SN, default=False)
    evid_cArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    evid_cObservacion = models.CharField(max_length=250, blank=True)

    registro_gastos = models.CharField(max_length=25, choices=acciones, default='No Aplica')
    registro_gArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    registro_gObservacion = models.CharField(max_length=250, blank=True)

    resumen_gastos = models.CharField(max_length=25, choices=acciones, default='No Aplica')
    resumen_gArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    resumen_gObservacion = models.CharField(max_length=250, blank=True)

    verificacion_sat = models.BooleanField(choices=SN, default=False)
    verificacionArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    verificacionObservacion = models.CharField(max_length=250, blank=True)

    xml = models.BooleanField(choices=SN, default=False)
    xmlArchivo = models.FileField(upload_to='PDF/SiSPRE/Cierre/', blank=True, null=True)
    xmlObservacion = models.CharField(max_length=250, blank=True)

    observacion = models.TextField(default='Sin observacion')

    def __str__(self):
        return '%s' % (self.estatus)

    class Meta:
        verbose_name_plural = "SISPRE Cierre"

class SISPRE (models.Model):
    inicio = models.ForeignKey(InicioS, on_delete=False)
    seguimiento = models.ForeignKey(SeguimientoS,on_delete=False)
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
    cct = models.CharField(max_length=11, verbose_name='C.C.T')
    nombre = models.CharField(max_length=250, verbose_name='Nombre de la Escuela')
    nivel = models.CharField(max_length=50, choices=nivelE,verbose_name='Nivel Educativo')
    componente = models.CharField(max_length=50, choices=comp, verbose_name='Componente')
    accion = models.CharField(max_length=25,choices=acciones, default='No Aplica',verbose_name='Accion')
    cambio_comp = models.BooleanField(default=False, choices=SN, verbose_name='Cambio de Componente')
    ciclo_esc = models.CharField(max_length=100,default="2017-2018")
    municipio = models.CharField(max_length=50,choices=Municipios)
    localidad = models.CharField(max_length=250)
    director = models.ForeignKey(Directores, on_delete=False)
    monto_asignado = models.FloatField()
    monto_ejercido = models.FloatField(default=0)
    #observacion = models.TextField(default='Sin observación')
    sispre = models.ForeignKey(SISPRE,on_delete=False)
    #contraloria_s = models.ForeignKey(Contraloria_Social)
    creacion = models.DateTimeField(auto_now=True)
    actualizacion = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.cct +' - '+self.nombre

    def __str__(self):
        return '%s - %s' % (self.cct, self.nombre)

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
    admin = models.BooleanField(choices=SN,default=False)
    escuela = models.ForeignKey(Escuelas, blank=True,null=True,on_delete=False)
    director = models.ForeignKey(Directores, blank=True,null=True,on_delete=False)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    instance.perfil.save()
