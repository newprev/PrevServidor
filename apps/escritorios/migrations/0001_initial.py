# Generated by Django 3.2.1 on 2021-11-06 14:09

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escritorio',
            fields=[
                ('escritorioId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nomeEscritorio', models.CharField(max_length=50, unique=True)),
                ('nomeFantasia', models.CharField(blank=True, max_length=50)),
                ('cnpj', models.CharField(blank=True, max_length=14, null=True, unique=True)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('inscEstadual', models.CharField(blank=True, max_length=9, null=True, unique=True)),
                ('endereco', models.CharField(blank=True, max_length=80)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('cep', models.CharField(blank=True, max_length=8)),
                ('complemento', models.CharField(blank=True, max_length=50)),
                ('cidade', models.CharField(blank=True, max_length=30)),
                ('estado', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='SP', max_length=2)),
                ('bairro', models.CharField(blank=True, max_length=50)),
                ('ativo', models.BooleanField(default=True)),
                ('qtdChaves', models.IntegerField(default=0)),
                ('dataUltAlt', models.DateTimeField(default=datetime.datetime(2021, 11, 6, 11, 9, 26, 310724))),
                ('dataCadastro', models.DateTimeField(default=datetime.datetime(2021, 11, 6, 11, 9, 26, 310741))),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
