from datetime import datetime

from django.utils import timezone
from ..escritorios.models import Escritorio
from django.db import models


class Advogado(models.Model):

    advogadoId = models.AutoField(primary_key=True, auto_created=True)
    escritorioId = models.ForeignKey(Escritorio, on_delete=models.CASCADE)
    senha = models.CharField(max_length=30, null=False, blank=False)
    login = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=40, null=False, blank=False)
    numeroOAB = models.CharField(max_length=9, null=False, blank=False, unique=True)
    cpf = models.CharField(max_length=11, null=False, blank=False, unique=True)
    nomeUsuario = models.CharField(max_length=20, null=False, blank=False)
    sobrenomeUsuario = models.CharField(max_length=40, null=False, blank=False)
    nacionalidade = models.CharField(max_length=40, default='brasileiro', null=False, blank=False)
    estadoCivil = models.CharField(max_length=20, default='solteiro', null=False, blank=False)
    admin = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    confirmado = models.BooleanField(default=False)
    dataUltAlt = models.DateTimeField(default=timezone.now, null=False)
    dataCadastro = models.DateTimeField(default=timezone.now, null=False)

    class Meta:
        db_table = "Advogados"

    def __str__(self):
        return f"id: {self.advogadoId}, nome: {self.nomeUsuario}, email: {self.email}, OAB: {self.numeroOAB}"


class PrimeiroAcesso(models.Model):

    TIPO = (
        ('C', 'CPF'),
        ('E', 'Email')
    )

    acessoId = models.AutoField(primary_key=True, auto_created=True)
    advogadoId = models.ForeignKey(Advogado, on_delete=models.CASCADE)
    codAcesso = models.IntegerField(null=False, blank=False)
    verificado = models.BooleanField(null=False, blank=False, default=False)
    tipoAcesso = models.CharField(max_length=1, choices=TIPO, default='C', null=False)
    dataUltAlt = models.DateTimeField(default=timezone.now, null=False)
    dataCadastro = models.DateTimeField(default=timezone.now, null=False)

    class Meta:
        db_table = "PrimeiroAcesso"
