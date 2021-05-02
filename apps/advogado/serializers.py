from rest_framework import serializers
from .models import Advogado

class AdvogadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advogado
        exclude = ['senha', 'dataUltAlt']

# class AdvByEscritorio(serializers.ModelSerializer):
#     class Meta:
#         model = Advogado