# Generated by Django 3.2 on 2021-05-02 01:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritorios', '0007_auto_20210501_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escritorio',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 1, 22, 30, 2, 413180)),
        ),
        migrations.AlterField(
            model_name='escritorio',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 1, 22, 30, 2, 413162)),
        ),
    ]
