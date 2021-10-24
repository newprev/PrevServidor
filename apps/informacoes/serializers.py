from rest_framework import serializers
from .models import Indicadores, ExpectativaSobrevida, IndicesAtualizacaoMonetaria, SalarioMinimo


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
        fields = ['dataReferente', 'dib', 'fator']


class SalarioMinimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalarioMinimo
        fields = ['vigencia', 'baseLegal', 'valor']