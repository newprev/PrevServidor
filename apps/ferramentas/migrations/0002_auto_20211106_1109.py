# Generated by Django 3.2.1 on 2021-11-06 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferramentas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carenciaslei91',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 6, 11, 9, 26, 314020)),
        ),
        migrations.AlterField(
            model_name='carenciaslei91',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 6, 11, 9, 26, 314007)),
        ),
        migrations.AlterField(
            model_name='convmon',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 6, 11, 9, 26, 313366)),
        ),
        migrations.AlterField(
            model_name='convmon',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 6, 11, 9, 26, 313353)),
        ),
        migrations.AlterField(
            model_name='tetosprev',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 6, 11, 9, 26, 313722)),
        ),
        migrations.AlterField(
            model_name='tetosprev',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 6, 11, 9, 26, 313709)),
        ),
    ]