from datetime import datetime

from django.db import models


class Indicadores(models.Model):
    db_table = 'indicadores'

    indicadorId = models.CharField(max_length=20, primary_key=True)
    resumo = models.CharField(max_length=300, null=False, blank=False)
    descricao = models.TextField(max_length=2000, null=False, blank=False)
    fonte = models.CharField(max_length=300, null=False, blank=False)
    dataUltAlt = models.DateTimeField(default=datetime.now(), null=False)
    dataCadastro = models.DateTimeField(default=datetime.now(), null=False)

    def __str__(self):
        return f"indicadorId: {self.indicadorId}, resumo: {self.resumo}"


class ExpectativaSobrevida(models.Model):
    db_table = 'expSobrevida'

    infoId = models.AutoField(primary_key=True, unique=True, blank=False, auto_created=True)
    dataReferente = models.DateField(blank=False, null=False)
    idade = models.FloatField(help_text='Idade do cliente')
    expectativaSobrevida = models.FloatField(help_text='Expectativa de vida de homens e mulheres no Brasil')
    dataUltAlt = models.DateTimeField(default=datetime.now(), null=False)
    dataCadastro = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return f"infoId: {self.infoId}, dataReferente: {self.dataReferente}, idade: {self.idade}"
