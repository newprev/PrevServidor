from rest_framework import serializers
from .models import Indicadores


class IndicadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicadores
        fields = ['indicadorId', 'resumo', 'descricao', 'fonte', 'dataUltAlt']