from rest_framework import viewsets
from .serializers import ConvMonSerializer, TetosPrevSerializer, CarenciaLei91Serializer
from .models import ConvMon, TetosPrev, CarenciasLei91

from logs.logRest import logPrioridade
from prevEnums import Prioridade, TipoLog


class ConvMonViewSet(viewsets.ModelViewSet):
    """Exibe todas as correções monetárias cadastradas"""
    try:
        logPrioridade("GET::/convMon", tipoLog=TipoLog.rest)
        queryset = ConvMon.objects.all()
        serializer_class = ConvMonSerializer
    except Exception as err:
        logPrioridade("erro::/convMon", tipoLog=TipoLog.rest, priodiade=Prioridade.erro)


class TetosPrevViewSet(viewsets.ModelViewSet):
    """Exibe todos os tetos previdenciários cadastrados"""
    try:
        logPrioridade("GET::/tetosPrev", tipoLog=TipoLog.rest)
        queryset = TetosPrev.objects.all()
        serializer_class = TetosPrevSerializer
    except Exception as err:
        logPrioridade("erro::/tetosPrev", tipoLog=TipoLog.rest, priodiade=Prioridade.erro)


class CarenciasLei91ViewSet(viewsets.ModelViewSet):
    """Exibe todas as datas de implementação da alteração do tempo mínimo de contribuição
    para aposentadorias até o ano de 2011"""
    try:
        logPrioridade("GET::/carenciasLei91", tipoLog=TipoLog.rest)
        queryset = CarenciasLei91.objects.all()
        serializer_class = CarenciaLei91Serializer
    except Exception as err:
        logPrioridade("erro::/carenciasLei91", priodiade=Prioridade.erro)
