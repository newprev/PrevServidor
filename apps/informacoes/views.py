from rest_framework import viewsets
from .serializers import IndicadoresSerializer, ExpSobrevidaSerializer
from .models import Indicadores, ExpectativaSobrevida

class IndicadoresViewSet(viewsets.ModelViewSet):
    """Exibe todos os possíveis indicadores do CNIS"""
    queryset = Indicadores.objects.all()
    serializer_class = IndicadoresSerializer


class ExpectativaSobrevidaViewSet(viewsets.ModelViewSet):
    """Exibe todas as informações do IBGE pertinentes ao programa"""
    queryset = ExpectativaSobrevida.objects.all()
    serializer_class = ExpSobrevidaSerializer