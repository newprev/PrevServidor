from rest_framework import viewsets, filters
from ..models import Escritorio
from ..serializers import EscritoriosSerializer
from django_filters.rest_framework import DjangoFilterBackend

from logs.logRest import logPrioridade
from prevEnums import Prioridade, TipoLog


class EscritorioViewSet(viewsets.ModelViewSet):
    """Exibindo todos advogados cadastrados"""
    try:
        logPrioridade('GET::api/escritorio/', tipoLog=TipoLog.rest)
        queryset = Escritorio.objects.all()
        serializer_class = EscritoriosSerializer
        filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
        ordering_fields = ['nomeEscritorio']
        search_fields = ['nomeEscritorio', 'cnpj']
        filterset_fields = ['ativo']
    except Exception as err:
        logPrioridade('erro::api/escritorio/', tipoLog=TipoLog.rest, priodiade=Prioridade.warnings)
