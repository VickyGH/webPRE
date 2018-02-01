# Generated by Django 2.0 on 2018-01-30 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0014_auto_20180123_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.CharField(choices=[('Incompleto', 'Incompleto'), ('Completo', 'Completo')], default='Incompleto', max_length=20)),
                ('acta', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('acta_Archivo', models.FileField(blank=True, null=True, upload_to='Contraloria_S/Anual/')),
                ('acta_Observacion', models.CharField(blank=True, max_length=250)),
                ('minuta', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('minuta_Archivo', models.FileField(blank=True, null=True, upload_to='Contraloria_S/Anual/')),
                ('minuta_Observacion', models.CharField(blank=True, max_length=250)),
                ('lista', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('lista_Archivo', models.FileField(blank=True, null=True, upload_to='Contraloria_S/Anual/')),
                ('lista_Observacion', models.CharField(blank=True, max_length=250)),
                ('foto', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('foto_Archivo', models.FileField(blank=True, null=True, upload_to='Contraloria_S/Anual/Fotos/')),
                ('foto_Observacion', models.CharField(blank=True, max_length=250)),
                ('cd', models.CharField(choices=[('No', 'No'), ('Si', 'Si')], default='No', max_length=10)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='Contraloria_S/Anual/')),
                ('observacion', models.TextField(default='Sin observaciones')),
            ],
            options={
                'ordering': ['estatus'],
                'verbose_name_plural': 'Contraloria Social - Anual',
            },
        ),
        migrations.CreateModel(
            name='Cedula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.CharField(choices=[('Incompleto', 'Incompleto'), ('Completo', 'Completo')], default='Incompleto', max_length=20)),
                ('acta', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('acta_Archivo', models.FileField(blank=True, null=True, upload_to='Contraloria_S/Seguimiento/')),
                ('acta_Observacion', models.CharField(blank=True, max_length=250)),
                ('minuta', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('minuta_Archivo', models.FileField(blank=True, null=True, upload_to='Contraloria_S/Seguimiento/')),
                ('minuta_Observacion', models.CharField(blank=True, max_length=250)),
                ('lista', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('lista_Archivo', models.FileField(blank=True, null=True, upload_to='Contraloria_S/Seguimiento/')),
                ('lista_Observacion', models.CharField(blank=True, max_length=250)),
                ('foto', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('foto_Archivo', models.FileField(blank=True, null=True, upload_to='Contraloria_S/Seguimiento/Fotos/')),
                ('foto_Observacion', models.CharField(blank=True, max_length=250)),
                ('cd', models.CharField(choices=[('No', 'No'), ('Si', 'Si')], default='No', max_length=10)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='Contraloria_S/Seguimiento/')),
                ('observacion', models.TextField(default='Sin observaciones')),
            ],
            options={
                'ordering': ['estatus'],
                'verbose_name_plural': 'Contraloria Social - Cedula',
            },
        ),
        migrations.CreateModel(
            name='Constitucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.CharField(choices=[('Incompleto', 'Incompleto'), ('Completo', 'Completo')], default='Incompleto', max_length=20)),
                ('acta', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('acta_Archivo', models.FileField(blank=True, null=True, upload_to='Contraloria_S/Inicio/')),
                ('acta_Observacion', models.CharField(blank=True, max_length=250)),
                ('minuta', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('minuta_Archivo', models.FileField(blank=True, null=True, upload_to='Contraloria_S/Inicio/')),
                ('minuta_Observacion', models.CharField(blank=True, max_length=250)),
                ('lista', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('lista_Archivo', models.FileField(blank=True, null=True, upload_to='Contraloria_S/Inicio/')),
                ('lista_Observacion', models.CharField(blank=True, max_length=250)),
                ('foto', models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40)),
                ('foto_Archivo', models.FileField(blank=True, null=True, upload_to='Contraloria_S/Inicio/Fotos/')),
                ('foto_Observacion', models.CharField(blank=True, max_length=250)),
                ('cd', models.CharField(choices=[('No', 'No'), ('Si', 'Si')], default='No', max_length=10)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='Contraloria_S/Inicio/')),
                ('observacion', models.TextField(default='Sin observaciones')),
            ],
            options={
                'ordering': ['estatus'],
                'verbose_name_plural': 'Contraloria Social - Constitución',
            },
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='acta_aArchivo',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='acta_aObservacion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='acta_anual',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='acta_cArchivo',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='acta_cObservacion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='acta_constitucion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='acta_sArchivo',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='acta_sObservacion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='acta_seguimiento',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='cd_anual',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='cd_constitucion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='cd_seguimiento',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='estatusA',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='estatusC',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='estatusS',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='foto_aArchivo',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='foto_aObservacion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='foto_anual',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='foto_cArchivo',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='foto_cObservacion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='foto_constitucion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='foto_sArchivo',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='foto_sObservacion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='foto_seguimiento',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='lista_aArchivo',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='lista_aObservacion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='lista_anual',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='lista_cArchivo',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='lista_cObservacion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='lista_constitucion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='lista_sArchivo',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='lista_sObservacion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='lista_seguimiento',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='minuta_aArchivo',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='minuta_aObservacion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='minuta_anual',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='minuta_cArchivo',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='minuta_cObservacion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='minuta_constitucion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='minuta_sArchivo',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='minuta_sObservacion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='minuta_seguimiento',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='observacion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='pdf_anual',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='pdf_constitucion',
        ),
        migrations.RemoveField(
            model_name='contraloria_social',
            name='pdf_seguimiento',
        ),
        migrations.AlterField(
            model_name='cierres',
            name='estatus',
            field=models.CharField(choices=[('Incompleto', 'Incompleto'), ('Completo', 'Completo')], default='Incompleto', max_length=40),
        ),
        migrations.AddField(
            model_name='contraloria_social',
            name='anual',
            field=models.ForeignKey(default=1, on_delete=False, to='Admin.Anual'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contraloria_social',
            name='cedula',
            field=models.ForeignKey(default=1, on_delete=False, to='Admin.Cedula'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contraloria_social',
            name='constitucion',
            field=models.ForeignKey(default=1, on_delete=False, to='Admin.Constitucion'),
            preserve_default=False,
        ),
    ]
