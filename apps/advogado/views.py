from rest_framework import viewsets, generics
from .models import Advogado
from .serializers import AdvogadoSerializer


class AdvogadosViewSet(viewsets.ModelViewSet):
    """Exibindo todos advogados cadastrados"""
    queryset = Advogado.objects.all()
    serializer_class = AdvogadoSerializer

class ListaAdvogadosByEscritorio(generics.ListAPIView):
    """Exibindo os(as) advogados(as) de determinado escritório"""
    def get_queryset(self):
        queryset = Advogado.objects.filter(escritorioId_id=self.kwargs['pk'])
        return queryset
    serializer_class = AdvogadoSerializer
