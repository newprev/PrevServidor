# Generated by Django 3.2.1 on 2021-06-05 20:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferramentas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convmon',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 5, 17, 43, 22, 126345)),
        ),
        migrations.AlterField(
            model_name='convmon',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 5, 17, 43, 22, 126334)),
        ),
        migrations.AlterField(
            model_name='tetosprev',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 5, 17, 43, 22, 126692)),
        ),
        migrations.AlterField(
            model_name='tetosprev',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 5, 17, 43, 22, 126680)),
        ),
    ]
