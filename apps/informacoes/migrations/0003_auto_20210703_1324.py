# Generated by Django 3.2.1 on 2021-07-03 16:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informacoes', '0002_auto_20210703_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicadores',
            name='fonte',
            field=models.CharField(default='www.calculojuridico.com.br', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 13, 22, 52, 932185)),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 13, 22, 52, 932172)),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='resumo',
            field=models.CharField(max_length=300),
        ),
    ]
