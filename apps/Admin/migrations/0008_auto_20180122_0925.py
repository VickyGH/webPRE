# Generated by Django 2.0 on 2018-01-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_auto_20180120_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contraloria_social',
            name='acta_aArchivo',
            field=models.FileField(blank=True, null=True, upload_to='Contraloria_S/Anual/'),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='acta_cArchivo',
            field=models.FileField(blank=True, null=True, upload_to='Contraloria_S/Inicio/'),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='acta_sArchivo',
            field=models.FileField(blank=True, null=True, upload_to='Contraloria_S/Seguimiento/'),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='foto_aArchivo',
            field=models.FileField(blank=True, null=True, upload_to='Contraloria_S/Anual/Fotos/'),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='foto_cArchivo',
            field=models.FileField(blank=True, null=True, upload_to='Contraloria_S/Inicio/Fotos/'),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='foto_sArchivo',
            field=models.FileField(blank=True, null=True, upload_to='Contraloria_S/Seguimiento/Fotos/'),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='lista_aArchivo',
            field=models.FileField(blank=True, null=True, upload_to='Contraloria_S/Anual/'),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='lista_cArchivo',
            field=models.FileField(blank=True, null=True, upload_to='Contraloria_S/Inicio/'),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='lista_sArchivo',
            field=models.FileField(blank=True, null=True, upload_to='Contraloria_S/Seguimiento/'),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='minuta_aArchivo',
            field=models.FileField(blank=True, null=True, upload_to='Contraloria_S/Anual/'),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='minuta_cArchivo',
            field=models.FileField(blank=True, null=True, upload_to='Contraloria_S/Inicio/'),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='minuta_sArchivo',
            field=models.FileField(blank=True, null=True, upload_to='Contraloria_S/Seguimiento/'),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='pdf_anual',
            field=models.FileField(blank=True, null=True, upload_to='Contraloria_S/Anual/'),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='pdf_constitucion',
            field=models.FileField(blank=True, null=True, upload_to='Contraloria_S/Inicio/'),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='pdf_seguimiento',
            field=models.FileField(blank=True, null=True, upload_to='Contraloria_S/Seguimiento/'),
        ),
        migrations.AlterField(
            model_name='inicios',
            name='acta_pArchivo',
            field=models.FileField(blank=True, null=True, upload_to='SiSPRE/Inicio/'),
        ),
        migrations.AlterField(
            model_name='inicios',
            name='acuse_bArchivo',
            field=models.FileField(blank=True, null=True, upload_to='SiSPRE/Inicio/'),
        ),
        migrations.AlterField(
            model_name='inicios',
            name='acuse_pArchivo',
            field=models.FileField(blank=True, null=True, upload_to='SiSPRE/Inicio/'),
        ),
        migrations.AlterField(
            model_name='inicios',
            name='acuse_prog_aArchivo',
            field=models.FileField(blank=True, null=True, upload_to='SiSPRE/Inicio/'),
        ),
        migrations.AlterField(
            model_name='inicios',
            name='compromiso_cArchivo',
            field=models.FileField(blank=True, null=True, upload_to='SiSPRE/Inicio/'),
        ),
        migrations.AlterField(
            model_name='inicios',
            name='compromiso_iArchivo',
            field=models.FileField(blank=True, null=True, upload_to='SiSPRE/Inicio/'),
        ),
        migrations.AlterField(
            model_name='inicios',
            name='constancia_cArchivo',
            field=models.FileField(blank=True, null=True, upload_to='SiSPRE/Inicio/'),
        ),
        migrations.AlterField(
            model_name='inicios',
            name='contrato',
            field=models.CharField(choices=[('No Aplica', 'No Aplica'), ('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default='No Aplica', max_length=25),
        ),
        migrations.AlterField(
            model_name='inicios',
            name='contratoArchivo',
            field=models.FileField(blank=True, null=True, upload_to='SiSPRE/Inicio/'),
        ),
        migrations.AlterField(
            model_name='inicios',
            name='ife_cArchivo',
            field=models.FileField(blank=True, null=True, upload_to='SiSPRE/Inicio/'),
        ),
        migrations.AlterField(
            model_name='inicios',
            name='ife_pArchivo',
            field=models.FileField(blank=True, null=True, upload_to='SiSPRE/Inicio/'),
        ),
        migrations.AlterField(
            model_name='seguimientos',
            name='acta_cArchivo',
            field=models.FileField(blank=True, null=True, upload_to='SiSPRE/Seguimiento/'),
        ),
        migrations.AlterField(
            model_name='seguimientos',
            name='acta_circunstanciada',
            field=models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default='No Aplica', max_length=25),
        ),
        migrations.AlterField(
            model_name='seguimientos',
            name='acta_sArchivo',
            field=models.FileField(blank=True, null=True, upload_to='SiSPRE/Seguimiento/'),
        ),
        migrations.AlterField(
            model_name='seguimientos',
            name='acta_seguimiento',
            field=models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default='No', max_length=25),
        ),
        migrations.AlterField(
            model_name='seguimientos',
            name='evid_sArchivo',
            field=models.FileField(blank=True, null=True, upload_to='SiSPRE/Seguimiento/'),
        ),
        migrations.AlterField(
            model_name='seguimientos',
            name='evid_seguimiento',
            field=models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default='No', max_length=25),
        ),
        migrations.AlterField(
            model_name='seguimientos',
            name='sup_tArchivo',
            field=models.FileField(blank=True, null=True, upload_to='SiSPRE/Seguimiento/'),
        ),
        migrations.AlterField(
            model_name='seguimientos',
            name='sup_tecnica',
            field=models.CharField(choices=[('Sin Datos', 'Sin Datos'), ('En revisión', 'En revisión'), ('Corregir', 'Corregir'), ('Correcto', 'Correcto')], default='No Aplica', max_length=25),
        ),
    ]