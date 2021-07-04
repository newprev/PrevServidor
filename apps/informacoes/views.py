from rest_framework import viewsets
from .serializers import IndicadoresSerializer
from .models import Indicadores

class IndicadoresViewSet(viewsets.ModelViewSet):
    """Exibe todas as correções monetárias cadastradas"""
    queryset = Indicadores.objects.all()
    serializer_class = IndicadoresSerializer