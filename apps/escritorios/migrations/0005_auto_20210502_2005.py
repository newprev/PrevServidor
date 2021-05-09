# Generated by Django 3.2 on 2021-05-02 23:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritorios', '0004_auto_20210502_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escritorio',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 20, 5, 51, 250586)),
        ),
        migrations.AlterField(
            model_name='escritorio',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 20, 5, 51, 250571)),
        ),
        migrations.AlterField(
            model_name='escritorio',
            name='escritorioId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
