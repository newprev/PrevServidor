from rest_framework import viewsets, generics, filters
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404

from logs.logRest import logPrioridade
from .models import Advogado
from .serializers import AdvogadoSerializer, ConfirmaAdvogadoSerializer, AuthClientSerializer
from django_filters.rest_framework import DjangoFilterBackend

from prevEnums import Prioridade, TipoLog


class AdvogadosViewSet(viewsets.ModelViewSet):
    """Exibindo todos advogados cadastrados"""
    try:
        logPrioridade("GET::api/advogados", tipoLog=TipoLog.rest)
        queryset = Advogado.objects.all()
        serializer_class = AdvogadoSerializer
        filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
        ordering_fields = ['nomeUsuario']
        search_fields = ['numeroOAB', 'email']
        filterset_fields = ['ativo']

    except Exception as err:
        logPrioridade("GET::api/advogados", tipoLog=TipoLog.rest, priodiade=Prioridade.warnings)

class AdvogadosConfirmacaoViewSet(generics.RetrieveUpdateAPIView):
    """Exibindo senha provisória de advogado ainda não confirmado"""
    def get_queryset(self):
        queryset = None
        try:
            if len(self.kwargs) != 0:
                advogadoId = self.kwargs['pk']
                logPrioridade(f"GET::api/advogados/{advogadoId}/confirmacao/")
                queryset = Advogado.objects.filter(advogadoId=advogadoId)

            return queryset
        except Exception as err:
            logPrioridade(f"err::api/advogados/<advogadoId>/confirmacao/", priodiade=Prioridade.warnings)
            return HttpResponse(status=510)

    def get_object(self):
        return get_object_or_404(Advogado, pk=self.kwargs['pk'])

    def patch(self, request, *args, **kwargs):
        try:
            logPrioridade(f"PATCH::api/advogados/<advogadoId>/confirmacao/")
            advModel = self.get_object()
            advogado = ConfirmaAdvogadoSerializer(advModel, data=request.data, partial=True)
            if advogado.is_valid():
                logPrioridade(f"UPDATE::AdvogadosConfirmacaoViewSet - {advModel.advogadoId=}", tipoLog=TipoLog.banco)
                advogado.save()
                return JsonResponse(status=201, data=advogado.data)
            return JsonResponse(status=400, data="Parâmetros errados")
        except Exception as err:
            logPrioridade(f"err::api/advogados/<advogadoId>/confirmacao/")
            return HttpResponse(status=510)

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
            try:
                escritorioId = self.kwargs['pk']
                queryset = Advogado.objects.filter(escritorioId_id=escritorioId)
                logPrioridade(f"api/escritorio/{escritorioId}/advogado")
                return queryset

            except Exception as err:
                logPrioridade(f"err::api/escritorio/<int:pk>/advogado::{err}", priodiade=Prioridade.warnings)
                return HttpResponse(status=510)


    serializer_class = AdvogadoSerializer

class AuthPrevClient(generics.RetrieveAPIView):
    """Autenticando usuário do PrevCliente"""

    search_fields = ['numeroOAB', 'email']
    serializer_class = AuthClientSerializer

    def get_object(self):
        try:
            login = self.kwargs['login']
            if login is not None:
                if login.isdecimal():
                    logPrioridade(f'OAB::api/advogados/auth/{login}')
                    return get_object_or_404(Advogado, numeroOAB=self.kwargs['login'])
                else:
                    logPrioridade(f'Email::api/advogados/auth/{login}')
                    return get_object_or_404(Advogado, email=self.kwargs['login'], ativo=True)
            else:
                logPrioridade(f'api/advogados/auth/{login}')
                JsonResponse(status=400, data="Parâmetros errados")
        except Exception as err:
            logPrioridade(f'api/advogados/auth/<login>', priodiade=Prioridade.warnings)
            return HttpResponse(status=510)

    def get_queryset(self):
        queryset = self.get_object()
        return queryset

