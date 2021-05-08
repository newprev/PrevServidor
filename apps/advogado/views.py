from rest_framework import viewsets, generics, filters
from .models import Advogado
from .serializers import AdvogadoSerializer
from django_filters.rest_framework import DjangoFilterBackend


class AdvogadosViewSet(viewsets.ModelViewSet):
    """Exibindo todos advogados cadastrados"""
    queryset = Advogado.objects.all()
    serializer_class = AdvogadoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nomeUsuario']
    search_fields = ['numeroOAB', 'email']
    filterset_fields = ['ativo']


class ListaAdvogadosByEscritorio(generics.ListAPIView):
    """Exibindo os(as) advogados(as) de determinado escritório"""
    def get_queryset(self):
        queryset = None
        if len(self.kwargs) != 0:
            queryset = Advogado.objects.filter(escritorioId_id=self.kwargs['pk'])
        return queryset
    serializer_class = AdvogadoSerializer
