# Generated by Django 3.2.1 on 2021-07-03 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informacoes', '0003_auto_20210703_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicadores',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 13, 28, 22, 584413)),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 13, 28, 22, 584393)),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='descricao',
            field=models.TextField(max_length=2000),
        ),
    ]
