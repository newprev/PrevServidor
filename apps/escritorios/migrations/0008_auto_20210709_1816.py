# Generated by Django 3.2.1 on 2021-07-09 21:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritorios', '0007_auto_20210704_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escritorio',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 9, 18, 16, 22, 994839)),
        ),
        migrations.AlterField(
            model_name='escritorio',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 9, 18, 16, 22, 994817)),
        ),
    ]
