# Generated by Django 3.2 on 2021-05-04 04:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritorios', '0015_auto_20210503_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='escritorio',
            name='senha',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='escritorio',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 4, 1, 12, 19, 281809)),
        ),
        migrations.AlterField(
            model_name='escritorio',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 4, 1, 12, 19, 281789)),
        ),
    ]
