import os, django
from django.db import models

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PrevServidor.settings')
django.setup()

from faker import Faker
from apps.advogado.models import Advogado
from apps.escritorios.models import Escritorio
import random


def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        escritorioId = Escritorio.objects.get(escritorioId=random.randrange(1, 5))
        senha = str(random.randrange(2000, 10000))
        nomeUsuarioAux = fake.name()
        nomeUsuario: str = nomeUsuarioAux[:nomeUsuarioAux.find(' ')]
        sobrenomeUsuario = nomeUsuarioAux[nomeUsuarioAux.find(' '):]
        numeroOAB = str(random.randrange(100000000, 999999999))
        login = nomeUsuario.lower()
        email = '{}@{}'.format(nomeUsuario.lower(), fake.free_email_domain())
        email = email.replace(' ', '')
        ativo = random.choice([True, False])

        a = Advogado(
            escritorioId=escritorioId,
            senha=senha,
            login=login,
            email=email,
            numeroOAB=numeroOAB,
            nomeUsuario=nomeUsuario,
            sobrenomeUsuario=sobrenomeUsuario,
            ativo=ativo
        )
        a.save()


criando_pessoas(135)

