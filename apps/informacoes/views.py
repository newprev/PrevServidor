from rest_framework import viewsets

from .serializers import IndicadoresSerializer, ExpSobrevidaSerializer, IndicesAtuMonetariaSerializer, SalarioMinimoSerializer, IpcaMensalSerializer
from .models import Indicadores, ExpectativaSobrevida, IndicesAtualizacaoMonetaria, SalarioMinimo, IpcaMensal

from logs.logRest import logPrioridade
from prevEnums import Prioridade, TipoLog


class IndicadoresViewSet(viewsets.ModelViewSet):
    """Exibe todos os possíveis indicadores do CNIS"""
    try:
        logPrioridade("GET::/indicadores", tipoLog=TipoLog.rest)
        queryset = Indicadores.objects.all()
        serializer_class = IndicadoresSerializer
    except Exception as err:
        logPrioridade("erro::/indicadores", tipoLog=TipoLog.rest, priodiade=Prioridade.erro)


class ExpectativaSobrevidaViewSet(viewsets.ModelViewSet):
    """Exibe todas as informações do IBGE pertinentes ao programa"""
    try:
        logPrioridade("GET::/expSobrevida", tipoLog=TipoLog.rest)
        queryset = ExpectativaSobrevida.objects.all()
        serializer_class = ExpSobrevidaSerializer
    except Exception as err:
        logPrioridade("erro::/expSobrevida", tipoLog=TipoLog.rest, priodiade=Prioridade.erro)


class IndicesAtuMonetariaViewSet(viewsets.ModelViewSet):
    """Exibe todos os índices de atualização monetária para cálculo do benefício"""
    try:
        logPrioridade("GET::/indiceAtuMonetaria", tipoLog=TipoLog.rest)
        queryset = IndicesAtualizacaoMonetaria.objects.all()
        serializer_class = IndicesAtuMonetariaSerializer
    except Exception as err:
        logPrioridade("erro::/indiceAtuMonetaria", tipoLog=TipoLog.rest, priodiade=Prioridade.erro)


class SalarioMinimoViewSet(viewsets.ModelViewSet):
    """Exibe todos os salários mínimos (R$) no Brasil desde 1994"""
    try:
        logPrioridade("GET::/salarioMinimo", tipoLog=TipoLog.rest)
        queryset = SalarioMinimo.objects.all()
        serializer_class = SalarioMinimoSerializer
    except Exception as err:
        logPrioridade("erro::/salarioMinimo", tipoLog=TipoLog.rest, priodiade=Prioridade.erro)


class IpcaMensalViewSet(viewsets.ModelViewSet):
    """Exibe todos os IPCAs mensais desde Janeiro de 2011"""
    try:
        logPrioridade("GET::/ipcaMensal", tipoLog=TipoLog.rest)
        queryset = IpcaMensal.objects.all()
        serializer_class = IpcaMensalSerializer
    except Exception as err:
        logPrioridade("erro::/ipcaMensal", tipoLog=TipoLog.rest, priodiade=Prioridade.erro)
