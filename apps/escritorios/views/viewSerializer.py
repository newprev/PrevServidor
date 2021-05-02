from rest_framework import viewsets
from ..models import Escritorio
from ..serializers import EscritoriosSerializer


class EscritorioViewSet(viewsets.ModelViewSet):
    """Exibindo todos advogados cadastrados"""
    queryset = Escritorio.objects.all()
    serializer_class = EscritoriosSerializer