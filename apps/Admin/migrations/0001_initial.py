# Generated by Django 2.0.1 on 2018-01-16 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CierreS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.CharField(choices=[('Incompleto', 'Incompleto'), ('Completo', 'Completo')], default='Incompleto', max_length=20)),
                ('acta_cierre', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('acta_cArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Cierre/')),
                ('acta_cObservacion', models.CharField(blank=True, max_length=250)),
                ('acta_entrega', models.CharField(choices=[('No Aplica', 'No Aplica'), ('Mayor', 'Mayor'), ('Menor', 'Menor')], default='No Aplica', max_length=25)),
                ('acta_eArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Cierre/')),
                ('acta_eObservacion', models.CharField(blank=True, max_length=250)),
                ('acta_rendicion', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('acta_rArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Cierre/')),
                ('acta_rObservacion', models.CharField(blank=True, max_length=250)),
                ('facturas', models.CharField(choices=[('No Aplica', 'No Aplica'), ('Mayor', 'Mayor'), ('Menor', 'Menor')], default='No Aplica', max_length=25)),
                ('facturasArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Cierre/')),
                ('facturasObservacion', models.CharField(blank=True, max_length=250)),
                ('ficha_reintegro', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('ficha_rArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Cierre/')),
                ('ficha_rObservacion', models.CharField(blank=True, max_length=250)),
                ('form_inventario', models.CharField(choices=[('No Aplica', 'No Aplica'), ('Mayor', 'Mayor'), ('Menor', 'Menor')], default='No Aplica', max_length=25)),
                ('form_iArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Cierre/')),
                ('form_iObservacion', models.CharField(blank=True, max_length=250)),
                ('form_transferencia', models.CharField(choices=[('No Aplica', 'No Aplica'), ('Mayor', 'Mayor'), ('Menor', 'Menor')], default='No Aplica', max_length=25)),
                ('form_tArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Cierre/')),
                ('form_tObservacion', models.CharField(blank=True, max_length=250)),
                ('evid_obra_concluida', models.CharField(choices=[('No Aplica', 'No Aplica'), ('Mayor', 'Mayor'), ('Menor', 'Menor')], default='No Aplica', max_length=25)),
                ('evid_obraArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Cierre/')),
                ('evid_obraObservacion', models.CharField(blank=True, max_length=250)),
                ('evid_compras', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('evid_cArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Cierre/')),
                ('evid_cObservacion', models.CharField(blank=True, max_length=250)),
                ('registro_gastos', models.CharField(choices=[('No Aplica', 'No Aplica'), ('Mayor', 'Mayor'), ('Menor', 'Menor')], default='No Aplica', max_length=25)),
                ('registro_gArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Cierre/')),
                ('registro_gObservacion', models.CharField(blank=True, max_length=250)),
                ('resumen_gastos', models.CharField(choices=[('No Aplica', 'No Aplica'), ('Mayor', 'Mayor'), ('Menor', 'Menor')], default='No Aplica', max_length=25)),
                ('resumen_gArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Cierre/')),
                ('resumen_gObservacion', models.CharField(blank=True, max_length=250)),
                ('verificacion_sat', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('verificacionArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Cierre/')),
                ('verificacionObservacion', models.CharField(blank=True, max_length=250)),
                ('xml', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('xmlArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Cierre/')),
                ('xmlObservacion', models.CharField(blank=True, max_length=250)),
                ('observacion', models.TextField(default='Sin observacion')),
            ],
            options={
                'verbose_name_plural': 'SISPRE Cierre',
            },
        ),
        migrations.CreateModel(
            name='Contraloria_Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.CharField(choices=[('Incompleto', 'Incompleto'), ('Completo', 'Completo')], default='Incompleto', max_length=20)),
                ('acta_constitucion', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('minuta_constitucion', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('lista_constitucion', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('foto_constitucion', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('cd_constitucion', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('pdf_constitucion', models.FileField(blank=True, null=True, upload_to='PDF/Contraloria_S/Inicio/')),
                ('acta_seguimiento', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('minuta_seguimiento', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('lista_seguimiento', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('foto_seguimiento', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('cd_seguimiento', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('pdf_seguimiento', models.FileField(blank=True, null=True, upload_to='PDF/Contraloria_S/Seguimiento/')),
                ('acta_anual', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('minuta_anual', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('lista_anual', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('foto_anual', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('cd_anual', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('pdf_anual', models.FileField(blank=True, null=True, upload_to='PDF/Contraloria_S/Cierre/')),
                ('observacion', models.TextField(default='Sin observacion')),
                ('actualizacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Contraloria Social',
                'ordering': ['actualizacion'],
            },
        ),
        migrations.CreateModel(
            name='Directores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('a_paterno', models.CharField(max_length=100)),
                ('a_materno', models.CharField(max_length=100)),
                ('telefono', models.CharField(default='Sin Numero', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Directores',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Escuelas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cct', models.CharField(max_length=11, verbose_name='C.C.T')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre de la Escuela')),
                ('nivel', models.CharField(choices=[('INDÍGENA', 'INDÍGENA'), ('PREESCOLAR', 'PREESCOLAR'), ('PRIMARIA', 'PRIMARIA'), ('SECUNDARIA', 'SECUNDARIA')], max_length=50, verbose_name='Nivel Educativo')),
                ('componente', models.CharField(choices=[('1 - A INFRAESTRUCTURA', '1 - A INFRAESTRUCTURA'), ('2 - B AUT. GEST. ESCOLAR', '2 - B AUT. GEST. ESCOLAR'), ('2 - C EVAL. DE IMPACTO', '2 - C EVAL. DE IMPACTO')], max_length=50, verbose_name='Componente')),
                ('accion', models.CharField(choices=[('No Aplica', 'No Aplica'), ('Mayor', 'Mayor'), ('Menor', 'Menor')], default='No Aplica', max_length=25, verbose_name='Accion')),
                ('cambio_comp', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False, verbose_name='Cambio de Componente')),
                ('ciclo_esc', models.CharField(default='2017-2018', max_length=100)),
                ('municipio', models.CharField(choices=[('Balancán', 'Balancán'), ('Cárdenas', 'Cárdenas'), ('Centla', 'Centla'), ('Centro', 'Centro'), ('Comalcalco', 'Comalcalco'), ('Cunduacán', 'Cunduacán'), ('Emiliano Zapata', 'Emiliano Zapata'), ('Huimanguillo', 'Huimanguillo'), ('Jalapa', 'Jalapa'), ('Jalpa de Méndez', 'Jalpa de Méndez'), ('Jonuta', 'Jonuta'), ('Macuspana', 'Macuspana'), ('Nacajuca', 'Nacajuca'), ('Paraíso', 'Paraíso'), ('Tacotalpa', 'Tacotalpa'), ('Teapa', 'Teapa'), ('Tenosique', 'Tenosique')], max_length=50)),
                ('localidad', models.CharField(max_length=250)),
                ('monto_asignado', models.FloatField()),
                ('monto_ejercido', models.FloatField(default=0)),
                ('creacion', models.DateTimeField(auto_now=True)),
                ('actualizacion', models.DateTimeField(auto_now_add=True)),
                ('director', models.ForeignKey(on_delete=False, to='Admin.Directores')),
            ],
            options={
                'verbose_name_plural': 'Escuelas',
                'ordering': ['cct'],
            },
        ),
        migrations.CreateModel(
            name='InicioS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.CharField(choices=[('Incompleto', 'Incompleto'), ('Completo', 'Completo')], default='Incompleto', max_length=20)),
                ('acta_mancomunado', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('acta_mArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Inicio/')),
                ('acta_mObservacion', models.CharField(blank=True, max_length=250)),
                ('constancia_cepse', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('constancia_cArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Inicio/')),
                ('constancia_cObservacion', models.CharField(blank=True, max_length=250)),
                ('acta_planeacion', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('acta_pArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Inicio/')),
                ('acta_pObservacion', models.CharField(blank=True, max_length=250)),
                ('acuse_banco', models.CharField(choices=[('No Aplica', 'No Aplica'), ('Mayor', 'Mayor'), ('Menor', 'Menor')], default='No Aplica', max_length=25)),
                ('acuse_bArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Inicio/')),
                ('acuse_bObservacion', models.CharField(blank=True, max_length=250)),
                ('acuse_prog', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('acuse_pArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Inicio/')),
                ('acuse_pObservacion', models.CharField(blank=True, max_length=250)),
                ('acuse_prog_anterior', models.CharField(choices=[('No Aplica', 'No Aplica'), ('Mayor', 'Mayor'), ('Menor', 'Menor')], default='No Aplica', max_length=25)),
                ('acuse_prog_aArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Inicio/')),
                ('acuse_prog_aObservacion', models.CharField(blank=True, max_length=250)),
                ('compromiso_inmueble', models.CharField(choices=[('No Aplica', 'No Aplica'), ('Mayor', 'Mayor'), ('Menor', 'Menor')], default='No Aplica', max_length=25)),
                ('compromiso_iArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Inicio/')),
                ('compromiso_iObservacion', models.CharField(blank=True, max_length=250)),
                ('compromiso_comunidad', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('compromiso_cArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Inicio/')),
                ('compromiso_cObservacion', models.CharField(blank=True, max_length=250)),
                ('contrato', models.CharField(choices=[('No Aplica', 'No Aplica'), ('Mayor', 'Mayor'), ('Menor', 'Menor')], default='No Aplica', max_length=25)),
                ('contratoArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Inicio/')),
                ('contratoObservacion', models.CharField(blank=True, max_length=250)),
                ('ife_cepse', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('ife_cArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Inicio/')),
                ('ife_cObservacion', models.CharField(blank=True, max_length=250)),
                ('ife_plantel', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('ife_pArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Inicio/')),
                ('ife_pObservacion', models.CharField(blank=True, max_length=250)),
                ('comision_director', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('comision_dArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Inicio/')),
                ('comision_dObservacion', models.CharField(blank=True, max_length=250)),
                ('observacion', models.TextField(default='Sin observacion')),
                ('foto_fachada', models.ImageField(blank=True, default='Fotos/Fotos_Fachada/None/no-img.png', upload_to='Fotos/Fotos_Fachada/')),
            ],
            options={
                'verbose_name_plural': 'SISPRE Inicio',
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=False, to='Admin.Directores')),
                ('escuela', models.ForeignKey(blank=True, null=True, on_delete=False, to='Admin.Escuelas')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SeguimientoS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.CharField(choices=[('Incompleto', 'Incompleto'), ('Completo', 'Completo')], default='Incompleto', max_length=20)),
                ('acta_seguimiento', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('acta_sArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Seguimiento/')),
                ('acta_sObservacion', models.CharField(blank=True, max_length=250)),
                ('sup_tecnica', models.CharField(choices=[('No Aplica', 'No Aplica'), ('Mayor', 'Mayor'), ('Menor', 'Menor')], default='No Aplica', max_length=25)),
                ('sup_tArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Seguimiento/')),
                ('sup_tObservacion', models.CharField(blank=True, max_length=250)),
                ('evid_seguimiento', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('evid_sArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Seguimiento/')),
                ('evid_sObservacion', models.CharField(blank=True, max_length=250)),
                ('acta_circunstanciada', models.CharField(choices=[('No Aplica', 'No Aplica'), ('Mayor', 'Mayor'), ('Menor', 'Menor')], default='No Aplica', max_length=25)),
                ('acta_cArchivo', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/Seguimiento/')),
                ('acta_cObservacion', models.CharField(blank=True, max_length=250)),
                ('observacion', models.TextField(default='Sin observacion')),
            ],
            options={
                'verbose_name_plural': 'SISPRE Seguimiento',
            },
        ),
        migrations.CreateModel(
            name='SISPRE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdfCompleto', models.FileField(blank=True, null=True, upload_to='PDF/SiSPRE/')),
                ('actualizacion', models.DateTimeField(auto_now_add=True)),
                ('cierre', models.ForeignKey(on_delete=False, to='Admin.CierreS')),
                ('inicio', models.ForeignKey(on_delete=False, to='Admin.InicioS')),
                ('seguimiento', models.ForeignKey(on_delete=False, to='Admin.SeguimientoS')),
            ],
            options={
                'verbose_name_plural': 'SiSPRE',
                'ordering': ['actualizacion'],
            },
        ),
        migrations.CreateModel(
            name='Supervisores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cct', models.CharField(max_length=11)),
                ('nombre', models.CharField(max_length=100)),
                ('a_paterno', models.CharField(max_length=100)),
                ('a_materno', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('zona_escolar', models.IntegerField()),
                ('escuelas_zona', models.ManyToManyField(to='Admin.Escuelas')),
            ],
            options={
                'verbose_name_plural': 'Supervisores',
                'ordering': ['cct'],
            },
        ),
        migrations.AddField(
            model_name='escuelas',
            name='sispre',
            field=models.ForeignKey(on_delete=False, to='Admin.SISPRE'),
        ),
    ]
