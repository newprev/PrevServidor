from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import auth, messages

# Create your views here.
from apps.escritorios.models import Escritorio
from apps.advogado.models import Advogado

from ..forms import AdvForm

from apps.escritorios.views.escritorioTools import *

from logs.logRest import logPrioridade
from prevEnums import TipoLog, Prioridade


def index(request):
    return render(request, 'index.html')


def cadastro(request):
    if request.method == 'POST':
        logPrioridade('POST::/cadastro', tipoLog=TipoLog.rest)
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        confirmaSenha = request.POST['confimacaoSenha']
        email = request.POST['email']
        licencas = request.POST['licencas']
        print('1 - ', usuario, senha, confirmaSenha, email, licencas)

        # Validação de usuário
        if campoVazio(usuario):
            messages.error(request, 'Usuário não pode ser vazio')
            return redirect('cadastro')

        if Escritorio.objects.filter(username=usuario).exists():
            messages.error(request, 'Usuário/Escritório já cadastrado por outro usuário !!!')
            return redirect('cadastro')

        # Validação de email
        if campoVazio(email):
            messages.error(request, 'Email já cadastrado por outro usuário !!!')
            return redirect('cadastro')

        if Escritorio.objects.filter(email=email).exists():
            print('Email Usuario já cadastrado')
            return redirect('cadastro')

        # Validação de senha
        if senhasIguais(senha, confirmaSenha):
            messages.error(request, 'As Senhas não são iguais')
            return redirect('cadastro')

        # Criando e Cadastrando novo usuario/escritorio
        escritorio = Escritorio.objects.create_user(
            username=usuario, nomeEscritorio=usuario, email=email, password=senha, qtdChaves=licencas, is_staff=False
        )
        logPrioridade(f"INSERT::cadastro - {escritorio.escritorioId=}", tipoLog=TipoLog.banco)
        escritorio.save()

        messages.success(request, 'Usuário cadastrado com sucesso !!!')

        return redirect('login')
    else:
        return render(request, 'cadastro.html')


def login(request):
    if request.method == 'POST':
        logPrioridade("POST::/login", tipoLog=TipoLog.rest)
        usuario = request.POST['usuario']
        senha = request.POST['senha']

        # if usuario == "" or senha == "":
        #     return redirect('login')

        if campoVazio(usuario):
            messages.error(request, "O campo  'USUÁRIO' não pode estar vazio")
            return redirect('login')

        if campoVazio(senha):
            messages.error(request, "O campo  'SENHA' não pode estar vazio")
            return redirect('login')

        if Escritorio.objects.filter(nomeEscritorio=usuario).exists():
            nome = Escritorio.objects.filter(nomeEscritorio=usuario).values_list('nomeEscritorio', flat=True)

            escritorio = auth.authenticate(request, username=nome[0], password=senha)

            if escritorio is not None:
                auth.login(request, escritorio)
                if not request.user.cpf:
                    messages.info(request, 'Ainda Faltam algumas informaçõe spara seu cadastro estar completo')
                else:
                    messages.success(request, 'Login Realizado Com Sucesso')
                return redirect('dashboard', escritorio.nomeEscritorio)
            else:
                messages.error(request, "SENHA INVÁLIDA")
        else:
            messages.error(request, "Não encontramos nenhum 'USUÁRIO' com este nome ")
    return render(request, 'login.html')


def logout(request):
    logPrioridade("POST::/logout", tipoLog=TipoLog.rest)
    auth.logout(request)
    return render(request, 'index.html')


def dashboard(request, nomeEscritorio):
    logPrioridade("GET::/dashboard", tipoLog=TipoLog.rest)

    if request.user.is_authenticated:

        if request.user.cpf is None:
            messages.info(request, 'Ainda FAlta algumas informaçõe spara seu cadastro estar completo')

        idUsuarioAtual = request.user.escritorioId
        chavesTotais = request.user.qtdChaves
        advCadstrado = Advogado.objects.filter(escritorioId=idUsuarioAtual)

        chaves = {}
        dicioChaves = {}

        if Advogado.objects.filter(escritorioId=idUsuarioAtual).exists():
            dicioChaves["advogados"] = advCadstrado

        for chave in range(1, (chavesTotais + 1) - len(advCadstrado)):
            if chave <= len(advCadstrado):
                chaves[chave] = advCadstrado[chave - 1]
            else:
                chaves[chave] = 'Cadastrar'

        booTotalChaves = False
        if len(advCadstrado) < chavesTotais:
            booTotalChaves = True

        intChavesUsadas = len(advCadstrado)

        dicioChaves = {'advogados': advCadstrado, 'booTotalChaves': booTotalChaves, 'intChavesUsadas': intChavesUsadas}

        return render(request, 'dashboard.html', dicioChaves)
    return redirect('index')


def editaEscritorio(request, nomeEscritorio):
    logPrioridade(f"SELECT::editaEscritorio - {nomeEscritorio=}", tipoLog=TipoLog.banco)
    escritorioAtivo = get_object_or_404(Escritorio, pk=request.user.escritorioId, nomeEscritorio=nomeEscritorio)
    escritorioAtivoEditar = {'escritorio': escritorioAtivo}
    return render(request, 'atualiza_Escritorio.html', escritorioAtivoEditar)


def atualizaEscritorio(request):
    if request.method == 'POST':
        try:
            logPrioridade(f"POST::/atualizaEscritorio", tipoLog=TipoLog.rest)
            escritorioId = request.POST['escritorioId']

            logPrioridade(f"UPDATE::atualizaEscritorio - {escritorioId}", tipoLog=TipoLog.banco)
            update = Escritorio.objects.get(pk=escritorioId)

            #update.nomeUsuario = request.POST['nome']
            #update.sobrenomeUsuario = request.POST['sobrenome']
            update.nomeFantasia = request.POST['nomeFantasia']
            update.cnpj = request.POST['cnpj']
            update.cpf = request.POST['cpf']
            update.telefone = request.POST['telefone']
            update.email = request.POST['email']
            update.inscEstadual = request.POST['inscrEstadual']
            update.cep = request.POST['cep']
            update.endereco = request.POST['endereco']
            update.numero = request.POST['endNumero']
            update.complemento = request.POST['complemento']
            update.cidade = request.POST['cidade']
            update.bairro = request.POST['bairro']
            update.estado = request.POST['estado']

            update.save()
        except Exception as err:
            logPrioridade(f"erro::/atualizaEscritorio - {err=}", tipoLog=TipoLog.rest, priodiade=Prioridade.erro)
    return redirect('dashboard', request.user.nomeEscritorio)


def criaAdv(request):
    logPrioridade("POST::/novoAdv", tipoLog=TipoLog.rest)
    form = AdvForm(request.POST or None)

    if form.is_valid():
        try:
            novo = form.save(commit=False)
            logPrioridade(f"INSERT::criaAdv - {form=}", tipoLog=TipoLog.banco)

            novo.escritorioId = request.user
            novo.save()
            form.save()
            return redirect('dashboard', request.user.nomeEscritorio)

        except Exception as err:
            logPrioridade(f"err::/novoAdv - {err=}", tipoLog=TipoLog.rest, priodiade=Prioridade.erro)

    return render(request, 'cadAdv.html', {'form': form})


def editaAdv(request, advogadoId):
    cardAdv = get_object_or_404(Advogado, pk=advogadoId)
    form = AdvForm(request.POST or None)
    cardAdvEditar = {'adv': cardAdv}
    return render(request, 'atualiza_adv.html', cardAdvEditar)


def atualizaAdv(request):
    try:
        if request.method == 'POST':
            logPrioridade("POST::/atualizaAdv", tipoLog=TipoLog.rest)
            advogadoId = request.POST['advogadoId']

            update = Advogado.objects.get(pk=advogadoId)

            update.nomeUsuario = request.POST['nome']
            update.sobrenomeUsuario = request.POST['sobrenome']
            update.numeroOAB = request.POST['oab']
            update.login = request.POST['login']
            update.senha = request.POST['senha']
            update.email = request.POST['email']
            update.nacionalidade = request.POST['nacionalidade']
            update.estadoCivil = request.POST['estadoCivil']
            update.ativo = request.POST.get('ativo')
            update.ativo = True if update.ativo else False

            logPrioridade(f"UPDATE::atualizaAdv - {update.nomeUsuario}", tipoLog=TipoLog.banco)
            update.save()

    except Exception as err:
        logPrioridade("erro::/atualizaAdv", tipoLog=TipoLog.rest, priodiade=Prioridade.erro)

    return redirect('dashboard', request.user.nomeEscritorio)


def deletaAdv(request, advogadoId):
    logPrioridade(f"DELETE::deletaAdv - {advogadoId}", tipoLog=TipoLog.rest)
    cardAdv = get_object_or_404(Advogado, pk=advogadoId)
    # --------------------------------------------------------------Estou comentando o metodo que deleta o advs
    cardAdv.delete()
    return redirect('dashboard', request.user.nomeEscritorio)

