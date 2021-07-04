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
