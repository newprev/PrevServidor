from rest_framework import serializers
from .models import ConvMon, TetosPrev


class ConvMonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConvMon
        exclude = ['convMonId', 'dataUltAlt', 'dataCadastro']


class TetosPrevSerializer(serializers.ModelSerializer):
    class Meta:
        model = TetosPrev
        exclude = ['dataValidade', 'dataCadastro']