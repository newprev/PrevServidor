from datetime import datetime
from django.db import models


class ConvMon(models.Model):
    db_table = 'convMon'

    CONVERSAO = (
        ('V', 'Valorizou'),
        ('D', 'Desvalorizou')
    )

    convMonId = models.AutoField(primary_key=True)
    nomeMoeda = models.CharField(max_length=20, blank=False)
    fator = models.BigIntegerField()
    dataInicial = models.DateTimeField(blank=False)
    dataFinal = models.DateTimeField(blank=True, null=True)
    conversao = models.CharField(max_length=1, choices=CONVERSAO, default='V', null=False)
    moedaCorrente = models.BooleanField(default=False)
    sinal = models.CharField(max_length=10, blank=False)
    dataUltAlt = models.DateTimeField(default=datetime.now())
    dataCadastro = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.nomeMoeda


class TetosPrev(models.Model):
    db_table = 'tetosPrev'

    tetosPrevId = models.AutoField(primary_key=True)
    dataValidade = models.DateTimeField(blank=False)
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    dataUltAlt = models.DateTimeField(default=datetime.now())
    dataCadastro = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.dataValidade


class CarenciasLei91(models.Model):
    db_table = 'carenciasLei91'

    carenciaId = models.AutoField(primary_key=True)
    dataImplemento = models.DateField(blank=False, null=False)
    tempoContribuicao = models.IntegerField(blank=False, null=False)
    dataUltAlt = models.DateTimeField(default=datetime.now())
    dataCadastro = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.dataImplemento}"
