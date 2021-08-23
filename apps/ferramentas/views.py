from rest_framework import viewsets
from .serializers import ConvMonSerializer, TetosPrevSerializer, CarenciaLei91Serializer
from .models import ConvMon, TetosPrev, CarenciasLei91


class ConvMonViewSet(viewsets.ModelViewSet):
    """Exibe todas as correções monetárias cadastradas"""
    queryset = ConvMon.objects.all()
    serializer_class = ConvMonSerializer


class TetosPrevViewSet(viewsets.ModelViewSet):
    """Exibe todos os tetos previdenciários cadastrados"""
    queryset = TetosPrev.objects.all()
    serializer_class = TetosPrevSerializer


class CarenciasLei91ViewSet(viewsets.ModelViewSet):
    """Exibe todas as datas de implementação da alteração do tempo mínimo de contribuição
    para aposentadorias até o ano de 2011"""
    queryset = CarenciasLei91.objects.all()
    serializer_class = CarenciaLei91Serializer
