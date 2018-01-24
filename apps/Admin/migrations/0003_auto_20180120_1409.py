# Generated by Django 2.0 on 2018-01-20 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_auto_20180118_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cierres',
            name='acta_cierre',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='cierres',
            name='acta_rendicion',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='cierres',
            name='evid_compras',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='cierres',
            name='ficha_reintegro',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='cierres',
            name='observacion',
            field=models.TextField(default='Sin observaciones'),
        ),
        migrations.AlterField(
            model_name='cierres',
            name='verificacion_sat',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='cierres',
            name='xml',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='acta_anual',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='acta_constitucion',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='acta_seguimiento',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='cd_anual',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='cd_constitucion',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='cd_seguimiento',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='foto_anual',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='foto_constitucion',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='foto_seguimiento',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='lista_anual',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='lista_constitucion',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='lista_seguimiento',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='minuta_anual',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='minuta_constitucion',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='minuta_seguimiento',
            field=models.BooleanField(choices=[('No', 'No'), ('Si', 'Si')], default=False),
        ),
        migrations.AlterField(
            model_name='contraloria_social',
            name='observacion',
            field=models.TextField(default='Sin observaciones'),
        ),
        migrations.AlterField(
            model_name='escuelas',
            name='cambio_comp',
            field=models.CharField(choices=[('No', 'No'), ('Si', 'Si')], default='No', max_length=25, verbose_name='Cambio de Componente'),
        ),
        migrations.AlterField(
            model_name='escuelas',
            name='componente',
            field=models.CharField(choices=[('1 - A Infraestructura', '1 - A Infraestructura'), ('2 - B Aut. Gest. Escolar', '2 - B Aut. Gest. Escolar'), ('2 - C Eval. de Impacto', '2 - C Eval. de Impacto')], default='2 - B Aut. Gest. Escolar', max_length=50, verbose_name='Componente'),
        ),
        migrations.AlterField(
            model_name='escuelas',
            name='nivel',
            field=models.CharField(choices=[('Indígena', 'Indígena'), ('Preescolar', 'Preescolar'), ('Primaria', 'Primaria'), ('Secundaria', 'Secundaria')], max_length=50, verbose_name='Nivel Educativo'),
        ),
        migrations.AlterField(
            model_name='escuelas',
            name='observacion',
            field=models.TextField(default='Sin observaciones'),
        ),
        migrations.AlterField(
            model_name='inicios',
            name='observacion',
            field=models.TextField(default='Sin observaciones'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='admin',
            field=models.CharField(default='No', max_length=25),
        ),
        migrations.AlterField(
            model_name='seguimientos',
            name='acta_seguimiento',
            field=models.CharField(default='No', max_length=25),
        ),
        migrations.AlterField(
            model_name='seguimientos',
            name='estatus',
            field=models.CharField(choices=[('Incompleto', 'Incompleto'), ('Completo', 'Completo'), ('No Aplica', 'No Aplica')], default='Incompleto', max_length=20),
        ),
        migrations.AlterField(
            model_name='seguimientos',
            name='evid_seguimiento',
            field=models.CharField(default='No', max_length=25),
        ),
        migrations.AlterField(
            model_name='seguimientos',
            name='observacion',
            field=models.TextField(default='Sin observaciones'),
        ),
    ]