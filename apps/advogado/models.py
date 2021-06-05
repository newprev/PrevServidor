from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from ..escritorios.models import Escritorio
from django.contrib import admin


class Advogado(models.Model):
    db_table = 'advogado'

    advogadoId = models.AutoField(primary_key=True, auto_created=True)
    escritorioId = models.ForeignKey(Escritorio, on_delete=models.CASCADE)
    senha = models.CharField(max_length=30, null=False, blank=False)
    login = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=40, null=False, blank=False)
    numeroOAB = models.CharField(max_length=9, null=False, blank=False, unique=True)
    nomeUsuario = models.CharField(max_length=20, null=False, blank=False)
    sobrenomeUsuario = models.CharField(max_length=40, null=False, blank=False)
    nacionalidade = models.CharField(max_length=40, default='brasileiro', null=False, blank=False)
    estadoCivil = models.CharField(max_length=20, default='solteiro', null=False, blank=False)
    admin = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    confirmado = models.BooleanField(default=False)
    dataUltAlt = models.DateTimeField(default=datetime.now(), null=False)
    dataCadastro = models.DateTimeField(default=datetime.now(), null=False)

    def __str__(self):
        return f"id: {self.advogadoId}, nome: {self.nomeUsuario}, email: {self.email}, OAB: {self.numeroOAB}"
        # return {'nome': self.nomeUsuario}


