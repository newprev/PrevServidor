# Generated by Django 3.2 on 2021-05-02 23:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritorios', '0008_auto_20210502_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escritorio',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 20, 46, 38, 532439)),
        ),
        migrations.AlterField(
            model_name='escritorio',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 20, 46, 38, 532423)),
        ),
    ]
