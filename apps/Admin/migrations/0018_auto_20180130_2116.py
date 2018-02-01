# Generated by Django 2.0 on 2018-01-31 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0017_auto_20180130_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escuelas',
            name='cambio_comp',
        ),
        migrations.AddField(
            model_name='escuelas',
            name='cambio_accion',
            field=models.CharField(choices=[('No', 'No'), ('Si', 'Si')], default='No', max_length=25, verbose_name='Cambio de Acción'),
        ),
        migrations.AlterField(
            model_name='escuelas',
            name='accion',
            field=models.CharField(choices=[('Mayor', 'Mayor'), ('Menor', 'Menor')], default='Menor', max_length=25, verbose_name='Accion'),
        ),
        migrations.AlterField(
            model_name='escuelas',
            name='componente',
            field=models.CharField(choices=[('2 - Aut. Gest. Escolar', '2 - Aut. Gest. Escolar')], default='2 - Aut. Gest. Escolar', max_length=50, verbose_name='Componente'),
        ),
        migrations.AlterField(
            model_name='inicios',
            name='acuse_banco',
            field=models.CharField(choices=[('No Aplica', 'No Aplica'), ('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default='No Aplica', max_length=25),
        ),
        migrations.AlterField(
            model_name='inicios',
            name='acuse_prog_anterior',
            field=models.CharField(choices=[('No Aplica', 'No Aplica'), ('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default='No Aplica', max_length=25),
        ),
        migrations.AlterField(
            model_name='inicios',
            name='compromiso_inmueble',
            field=models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default='No Aplica', max_length=25),
        ),
    ]
