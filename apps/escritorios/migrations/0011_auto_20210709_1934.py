# Generated by Django 3.2.1 on 2021-07-09 22:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritorios', '0010_auto_20210709_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escritorio',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 9, 19, 34, 39, 282700)),
        ),
        migrations.AlterField(
            model_name='escritorio',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 9, 19, 34, 39, 282679)),
        ),
    ]
