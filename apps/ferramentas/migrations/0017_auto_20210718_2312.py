# Generated by Django 3.2.1 on 2021-07-19 02:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferramentas', '0016_auto_20210718_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convmon',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 18, 23, 12, 43, 883468)),
        ),
        migrations.AlterField(
            model_name='convmon',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 18, 23, 12, 43, 883451)),
        ),
        migrations.AlterField(
            model_name='tetosprev',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 18, 23, 12, 43, 883876)),
        ),
        migrations.AlterField(
            model_name='tetosprev',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 18, 23, 12, 43, 883859)),
        ),
    ]