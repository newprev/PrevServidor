from rest_framework import serializers
from .models import Escritorio

class EscritoriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escritorio
        exclude = ['dataUltAlt']