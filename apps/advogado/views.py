from rest_framework import viewsets, generics, filters
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Advogado
from .serializers import AdvogadoSerializer, ConfirmaAdvogadoSerializer, AuthClientSerializer
from django_filters.rest_framework import DjangoFilterBackend


class AdvogadosViewSet(viewsets.ModelViewSet):
    """Exibindo todos advogados cadastrados"""
    queryset = Advogado.objects.all()
    serializer_class = AdvogadoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nomeUsuario']
    search_fields = ['numeroOAB', 'email']
    filterset_fields = ['ativo']

class AdvogadosConfirmacaoViewSet(generics.RetrieveUpdateAPIView):
    """Exibindo senha provisória de advogado ainda não confirmado"""
    def get_queryset(self):
        queryset = None
        if len(self.kwargs) != 0:
            queryset = Advogado.objects.filter(advogadoId=self.kwargs['pk'])
        return queryset

    def get_object(self):
        return get_object_or_404(Advogado, pk=self.kwargs['pk'])

    def patch(self, request, *args, **kwargs):
        advModel = self.get_object()
        advogado = ConfirmaAdvogadoSerializer(advModel, data=request.data, partial=True)
        if advogado.is_valid():
            advogado.save()
            return JsonResponse(status=201, data=advogado.data)
        return JsonResponse(status=400, data="Parâmetros errados")

    serializer_class = ConfirmaAdvogadoSerializer
    http_method_names = ['get', 'patch']

class ListaAdvogadosByEscritorio(generics.ListAPIView):
    """Exibindo os(as) advogados(as) de determinado escritório"""

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['login']
    filterset_fields = ['confirmado', 'ativo']

    def get_queryset(self):
        queryset = None
        if len(self.kwargs) != 0:
            queryset = Advogado.objects.filter(escritorioId_id=self.kwargs['pk'])
        return queryset
    serializer_class = AdvogadoSerializer

class AuthPrevClient(generics.RetrieveAPIView):
    """Autenticando usuário do PrevCliente"""

    search_fields = ['numeroOAB', 'email']
    serializer_class = AuthClientSerializer

    def get_object(self):
        login = self.kwargs['login']
        if login is not None:
            if login.isdecimal():
                return get_object_or_404(Advogado, numeroOAB=self.kwargs['login'])
            else:
                return get_object_or_404(Advogado, email=self.kwargs['login'], ativo=True)
        else:
            JsonResponse(status=400, data="Parâmetros errados")

    def get_queryset(self):
        queryset = self.get_object()
        return queryset

