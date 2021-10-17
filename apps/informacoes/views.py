from rest_framework import viewsets
from .serializers import IndicadoresSerializer, ExpSobrevidaSerializer, IndicesAtuMonetariaSerializer, SalarioMinimoSerializer
from .models import Indicadores, ExpectativaSobrevida, IndicesAtualizacaoMonetaria, SalarioMinimo


class IndicadoresViewSet(viewsets.ModelViewSet):
    """Exibe todos os possíveis indicadores do CNIS"""
    queryset = Indicadores.objects.all()
    serializer_class = IndicadoresSerializer


class ExpectativaSobrevidaViewSet(viewsets.ModelViewSet):
    """Exibe todas as informações do IBGE pertinentes ao programa"""
    queryset = ExpectativaSobrevida.objects.all()
    serializer_class = ExpSobrevidaSerializer


class IndicesAtuMonetariaViewSet(viewsets.ModelViewSet):
    """Exibe todos os índices de atualização monetária para cálculo do benefício"""
    queryset = IndicesAtualizacaoMonetaria.objects.all()
    serializer_class = IndicesAtuMonetariaSerializer


class SalarioMinimoViewSet(viewsets.ModelViewSet):
    """Exibe todos os salários mínimos (R$) no Brasil desde 1994"""
    queryset = SalarioMinimo.objects.all()
    serializer_class = SalarioMinimoSerializer
