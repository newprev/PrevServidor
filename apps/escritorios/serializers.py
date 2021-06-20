from rest_framework import serializers
from .models import Escritorio
from .validators import *


class EscritoriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escritorio
        exclude = []

    def validate(self, data):
        if not validaCpf(data['cpf']):
            raise serializers.ValidationError({"cpf": "CPF inválido."})

        if not validaCNPJ(data['cnpj']):
            raise serializers.ValidationError({"cnpj": "O CNPJ inválido"})

        return data
