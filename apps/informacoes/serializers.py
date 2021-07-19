from rest_framework import serializers
from .models import Indicadores, ExpectativaSobrevida, IndicesAtualizacaoMonetaria


class IndicadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicadores
        fields = ['indicadorId', 'resumo', 'descricao', 'fonte', 'dataUltAlt']


class ExpSobrevidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpectativaSobrevida
        exclude = ['dataUltAlt', 'dataCadastro']


class IndicesAtuMonetariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicesAtualizacaoMonetaria
        fields = ['dataReferente', 'fator']
