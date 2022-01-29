from dateutil.relativedelta import relativedelta

from rest_framework import viewsets, generics, filters
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend

from random import randint

from apps.newMails.views import primeiroAcessoAdvogado, trocouSenhaAdvogado
from logs.logRest import logPrioridade
from .models import Advogado, TrocaSenha
from .serializers import AdvogadoSerializer, ConfirmaAdvogadoSerializer, AuthClientSerializer, TrocaSenhaSerializer

from prevEnums import Prioridade, TipoLog, TipoTrocaSenha


class AdvogadosViewSet(viewsets.ModelViewSet):
    """Exibindo todos advogados cadastrados"""
    http_method_names = ['patch', 'get']

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

    def patch(self, request, *args, **kwargs):
        try:
            senha = request.data['senhaEnviada']
            advogadoId = request.data['advogadoId']

            advogado: Advogado = get_object_or_404(Advogado, advogadoId=advogadoId)
            advogado.senha = senha
            advogado.dataUltAlt = timezone.now()
            advogado.confirmado = True
            advogado.save()
            logPrioridade(f"UPDATE::AdvogadosConfirmacaoViewSet - {advogado=}", tipoLog=TipoLog.banco)
            return HttpResponse("Advogado atualizado", status=201)

        except Exception as err:
            print(f"{err=}")
            return HttpResponse('', status=500)

class AdvogadosConfirmacaoViewSet(generics.RetrieveUpdateAPIView):
    """Exibindo senha provisória de advogado ainda não confirmado"""
    def get_queryset(self):
        queryset = None
        try:
            if len(self.kwargs) != 0:
                advogadoId = self.kwargs['pk']
                logPrioridade(f"GET::api/advogados/{advogadoId}/confirmacao/", tipoLog=TipoLog.rest)
                queryset = Advogado.objects.filter(advogadoId=advogadoId)

            return queryset
        except Exception as err:
            logPrioridade(f"err::api/advogados/<advogadoId>/confirmacao/", tipoLog=TipoLog.erro, priodiade=Prioridade.erro)
            return HttpResponse(status=510)

    def get_object(self):
        return get_object_or_404(Advogado, pk=self.kwargs['pk'])

    def patch(self, request, *args, **kwargs):
        try:
            logPrioridade(f"PATCH::api/advogados/<advogadoId>/confirmacao/", tipoLog=TipoLog.rest)
            advModel = self.get_object()
            advogado = ConfirmaAdvogadoSerializer(advModel, data=request.data, partial=True)
            if advogado.is_valid():
                logPrioridade(f"UPDATE::AdvogadosConfirmacaoViewSet - {advModel.advogadoId=}", tipoLog=TipoLog.banco)
                advogado.save()
                return JsonResponse(status=201, data=advogado.data)
            return JsonResponse(status=400, data="Parâmetros errados")
        except Exception as err:
            logPrioridade(f"err::api/advogados/<advogadoId>/confirmacao/", tipoLog=TipoLog.erro)
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
                logPrioridade(f"api/escritorio/{escritorioId}/advogado", tipoLog=TipoLog.rest)
                return queryset

            except Exception as err:
                logPrioridade(f"err::api/escritorio/<int:pk>/advogado::{err}", tipoLog=TipoLog.rest, priodiade=Prioridade.warnings)
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
                    logPrioridade(f'OAB::api/advogados/auth/{login}', tipoLog=TipoLog.rest)
                    return get_object_or_404(Advogado, numeroOAB=self.kwargs['login'])
                else:
                    logPrioridade(f'Email::api/advogados/auth/{login}', tipoLog=TipoLog.rest)
                    return get_object_or_404(Advogado, email=self.kwargs['login'], ativo=True)
            else:
                logPrioridade(f'api/advogados/auth/{login}', tipoLog=TipoLog.rest)
                JsonResponse(status=400, data="Parâmetros errados")
        except Exception as err:
            logPrioridade(f'erro::api/advogados/auth/<login>', tipoLog=TipoLog.rest, priodiade=Prioridade.erro)
            return HttpResponse(status=510)

    def get_queryset(self):
        queryset = self.get_object()
        return queryset

class TrocaSenhaViewSet(generics.RetrieveUpdateAPIView):
    """Primeiro acesso do advogado pelo PrevCliente"""

    serializer_class = TrocaSenhaSerializer
    http_method_names = ['post', 'get']

    def verificaTipoBool(self, variavel) -> bool:
        if isinstance(variavel, bool):
            return variavel
        elif isinstance(variavel, str):
            return variavel == 'True'
        else:
            return False

    def post(self, request, **kwargs):
        try:
            logPrioridade(f"POST::api/advogados/auth/trocaSenha", tipoLog=TipoLog.rest)
            if request.data is not None:
                if 'esqueceuSenha' in request.data.keys():
                    esqueceuSenha = self.verificaTipoBool(request.data['esqueceuSenha'])
                else:
                    esqueceuSenha = False

                if 'info' in request.data.keys() and request.data['info'] is not None:
                    login = request.data['info']
                    if login is not None:
                        advogado: Advogado = self.get_object(login, esqueceuSenha=esqueceuSenha)
                        if advogado is not None:
                            trocaSenha = TrocaSenha()
                            trocaSenha.advogadoId = advogado
                            trocaSenha.primAcesso = not esqueceuSenha
                            trocaSenha.codAcesso = randint(10000, 99999)

                            if esqueceuSenha:
                                trocaSenha.tipoTroca = TipoTrocaSenha.EsqueceuSenha.value
                                advogado.confirmado = True
                                trocouSenhaAdvogado(advogado, trocaSenha)
                            else:
                                advogado.confirmado = False
                                trocaSenha.tipoTroca = TipoTrocaSenha.PrimeiroAcesso.value
                                primeiroAcessoAdvogado(advogado, trocaSenha)

                            advogado.save()
                            trocaSenha.save()
                            return JsonResponse({"advogadoId": advogado.advogadoId})
                        else:
                            return HttpResponse("Nenhum advogado encontrado", status=310)
                    else:
                        return HttpResponse("Não foi possível carregar o CPF/E-mail enviado", status=300)
        except Exception as err:
            print(err)
            logPrioridade(f'erro::POST::api/advogados/auth/trocaSenha/', tipoLog=TipoLog.rest, priodiade=Prioridade.erro)
            return HttpResponse(status=510)

    def get_object(self, infoRequest: str, esqueceuSenha: bool = False):
        info = infoRequest
        if info.isnumeric():
            queryset = get_object_or_404(Advogado, cpf=info, confirmado=esqueceuSenha)
        else:
            queryset = get_object_or_404(Advogado, email=info, confirmado=esqueceuSenha)

        return queryset

class AutenticaPrimeiroAcesso(generics.RetrieveUpdateAPIView):
    """Faz a autenticação do primeiro acesso por meio do código de acesso enviado por email"""

    serializer_class = TrocaSenhaSerializer
    http_method_names = ['patch', 'get']

    def get_queryset(self):
        queryset = None
        try:
            logPrioridade(f"GET::api/advogados/auth/autenticaCodAcesso/<int:codAcesso>", tipoLog=TipoLog.rest)
            queryset = TrocaSenha.objects.filter(verificado=True)

            return queryset
        except Exception as err:
            logPrioridade(f"err::api/advogados/auth/autenticaCodAcesso/<int:codAcesso>", tipoLog=TipoLog.erro, priodiade=Prioridade.erro)
            return HttpResponse(status=510)

    def patch(self, request, **kwargs):
        try:
            logPrioridade(f"PATCH::api/advogados/auth/autenticaCodAcesso/<int:codAcesso>", tipoLog=TipoLog.rest)

            if 'codigo' not in request.data.keys():
                logPrioridade(f'erro::api/advogados/auth/autenticaCodAcesso/<int:codAcesso>', tipoLog=TipoLog.rest, priodiade=Prioridade.erro)
                return HttpResponse(status=410)
            else:
                codigo = int(request.data['codigo'])
                if codigo is not None:
                    primAcesso: TrocaSenha = self.get_object(codigo)
                    if primAcesso is not None:
                        tempoDecorrido: relativedelta = relativedelta(timezone.now(), primAcesso.dataCadastro)
                        if tempoDecorrido.minutes > 10:
                            return HttpResponse("Tempo excedido. Tente novamente.", status=406)
                        else:
                            primAcesso.verificado = True
                            primAcesso.save()
                            return HttpResponse("Código de acesso confirmado.", status=201)
                else:
                    return HttpResponse("Chave incorreta", status=310)
        except Exception as err:
            print(err)
            logPrioridade(f'erro::api/advogados/auth/autenticaCodAcesso/<int:codAcesso>', tipoLog=TipoLog.rest, priodiade=Prioridade.erro)
            return HttpResponse(status=510)

    def get_object(self, codigo: int):
        return get_object_or_404(TrocaSenha, codAcesso=codigo, verificado=False)

