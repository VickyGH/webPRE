# Generated by Django 2.0 on 2018-01-31 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0015_auto_20180129_2114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anual',
            old_name='acta',
            new_name='actaA',
        ),
        migrations.RenameField(
            model_name='cedula',
            old_name='acta',
            new_name='actaCe',
        ),
        migrations.RenameField(
            model_name='constitucion',
            old_name='acta',
            new_name='actaC',
        ),
    ]
