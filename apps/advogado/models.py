from datetime import datetime

from django.db import models
from ..escritorios.models import Escritorio


class Advogado(models.Model):
    escritorioId = models.ForeignKey(Escritorio, models.CASCADE)
    senha = models.CharField(max_length=30, null=False, blank=False)
    login = models.CharField(max_length=30, null=False, blank=False)
    email = models.CharField(max_length=40, null=False, blank=False)
    numeroOAB = models.CharField(max_length=9, null=False, blank=False)
    nomeUsuario = models.CharField(max_length=20, null=False, blank=False)
    sobrenomeUsuario = models.CharField(max_length=40, null=False, blank=False)
    nacionalidade = models.CharField(max_length=40, default='brasileiro', null=False, blank=False)
    estadoCivil = models.CharField(max_length=20, default='solteiro', null=False, blank=False)
    admin = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    dataUltAlt = models.DateTimeField(default=datetime.now(), null=False)
    dataCadastro = models.DateTimeField(default=datetime.now(), null=False)

    def __str__(self):
        return self.nomeUsuario



