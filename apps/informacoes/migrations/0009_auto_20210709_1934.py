# Generated by Django 3.2.1 on 2021-07-09 22:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informacoes', '0008_auto_20210709_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpectativaSobrevida',
            fields=[
                ('infoId', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('dataReferente', models.DateField()),
                ('idade', models.FloatField(help_text='Idade do cliente')),
                ('expectativaSobrevida', models.FloatField(help_text='Expectativa de vida de homens e mulheres no Brasil')),
                ('dataUltAlt', models.DateTimeField(default=datetime.datetime(2021, 7, 9, 19, 34, 39, 286138))),
                ('dataCadastro', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='InfoIBGE',
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='dataCadastro',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 9, 19, 34, 39, 285880)),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='dataUltAlt',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 9, 19, 34, 39, 285866)),
        ),
    ]
