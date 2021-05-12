from rest_framework import serializers
from .models import Advogado
from .validators import *


class AdvogadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advogado
        exclude = ['senha', 'dataUltAlt']

    def validate(self, data):
        if not validaCpf(data['cpf']):
            raise serializers.ValidationError({"cpf": "CPF inválido."})

        if not validaTamanhoNumOAB(data['numeroOAB']):
            raise serializers.ValidationError({"numeroOAB": "O número da OAB precisa ter 9 dígitos."})

        if not validaApenasNumerosOAB(data['numeroOAB']):
            raise serializers.ValidationError({"numeroOAB": "O número da OAB deve conter apenas números."})

        if not validaNomeUsuario(data['nomeUsuario']):
            raise serializers.ValidationError({"nomeUsuario": "O nome do advogado não deve conter números."})

        if not validaSobrenomeUsuario(data['sobrenomeUsuario']):
            raise serializers.ValidationError({"sobrenomeUsuario": "O sobrenome do advogado não deve conter números."})

        return data

class ConfirmaAdvogadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advogado
        fields = ['senha', 'confirmado']
