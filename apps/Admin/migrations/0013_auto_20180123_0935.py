# Generated by Django 2.0 on 2018-01-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0012_auto_20180122_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cierres',
            name='acta_entrega',
            field=models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default='No Aplica', max_length=40),
        ),
        migrations.AlterField(
            model_name='cierres',
            name='acta_rendicion',
            field=models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40),
        ),
        migrations.AlterField(
            model_name='cierres',
            name='estatus',
            field=models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default='Incompleto', max_length=40),
        ),
        migrations.AlterField(
            model_name='cierres',
            name='evid_compras',
            field=models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40),
        ),
        migrations.AlterField(
            model_name='cierres',
            name='evid_obra_concluida',
            field=models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default='No Aplica', max_length=40),
        ),
        migrations.AlterField(
            model_name='cierres',
            name='facturas',
            field=models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default='No Aplica', max_length=40),
        ),
        migrations.AlterField(
            model_name='cierres',
            name='ficha_reintegro',
            field=models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40),
        ),
        migrations.AlterField(
            model_name='cierres',
            name='form_inventario',
            field=models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default='No Aplica', max_length=40),
        ),
        migrations.AlterField(
            model_name='cierres',
            name='form_transferencia',
            field=models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default='No Aplica', max_length=40),
        ),
        migrations.AlterField(
            model_name='cierres',
            name='registro_gastos',
            field=models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default='No Aplica', max_length=40),
        ),
        migrations.AlterField(
            model_name='cierres',
            name='resumen_gastos',
            field=models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default='No Aplica', max_length=40),
        ),
        migrations.AlterField(
            model_name='cierres',
            name='verificacion_sat',
            field=models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40),
        ),
        migrations.AlterField(
            model_name='cierres',
            name='xml',
            field=models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default=False, max_length=40),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='admin',
            field=models.CharField(choices=[('No', 'No'), ('Si', 'Si')], default='No', max_length=25),
        ),
    ]