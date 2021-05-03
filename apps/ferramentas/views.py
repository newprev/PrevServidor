from rest_framework import viewsets
from .serializers import ConvMonSerializer, TetosPrevSerializer
from .models import ConvMon, TetosPrev

class ConvMonViewSet(viewsets.ModelViewSet):
    """Exibe todas as correções monetárias cadastradas"""
    queryset = ConvMon.objects.all()
    serializer_class = ConvMonSerializer

class TetosPrevViewSet(viewsets.ModelViewSet):
    """Exibe todos os tetos previdenciários cadastrados"""
    queryset = TetosPrev.objects.all()
    serializer_class = TetosPrevSerializer