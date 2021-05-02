from datetime import datetime

from django.db import models
from utils.helpers import getEstados

class Escritorio(models.Model):
    ESTADO = getEstados()

    nomeEscritorio = models.CharField(max_length=50, blank=False)
    nomeFantasia = models.CharField(max_length=50, blank=True)
    cnpj = models.CharField(max_length=14, blank=True)
    cpf = models.CharField(max_length=11, blank=True)
    inscEstadual = models.CharField(max_length=9, blank=True)
    endereco = models.CharField(max_length=80, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    cep = models.CharField(max_length=8, blank=True)
    complemento = models.CharField(max_length=50, blank=True)
    cidade = models.CharField(max_length=30, blank=True)
    estado = models.CharField(max_length=2, choices=ESTADO, null=False, default='SP', blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    ativo = models.BooleanField(default=True)
    qtdChaves = models.IntegerField(default=0)
    dataUltAlt = models.DateTimeField(default=datetime.now(), null=False)
    dataCadastro = models.DateTimeField(default=datetime.now(), null=False)

    def __str__(self):
        return self.nomeEscritorio

