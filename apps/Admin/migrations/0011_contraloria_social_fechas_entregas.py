# Generated by Django 2.0 on 2018-01-22 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_auto_20180122_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='contraloria_social',
            name='fechas_entregas',
            field=models.ForeignKey(blank=True, null=True, on_delete=False, to='Admin.Fechas_Finales'),
        ),
    ]