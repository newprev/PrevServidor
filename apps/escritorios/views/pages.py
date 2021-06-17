from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import auth

# Create your views here.
from apps.escritorios.models import Escritorio
from apps.advogado.models import Advogado

from ..forms import AdvForm


def index(request):
    return render(request, 'index.html')


def cadastro(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        confirmaSenha = request.POST['confimacaoSenha']
        email = request.POST['email']
        licencas = request.POST['licencas']
        print('1 - ', usuario, senha, confirmaSenha, email, licencas)

        # Validação de usuário
        if not usuario.strip():
            print('O Usuário  não pode ficar em branco')
            return redirect('cadastro')

        if Escritorio.objects.filter(username=usuario).exists():
            print('=--------------------------------------USUARIO ja Cadastrado')
            return redirect('cadastro')

        # Validação de email
        if not email.strip():
            print('O Email  não pode ficar em branco')
            return redirect('cadastro')

        # Validação de senha
        if senha != confirmaSenha:
            print('As senhas digitadas não são iguais')
            return redirect('cadastro')

        # Validação de usuário existente no banco
        if Escritorio.objects.filter(email=email).exists():
            print('Email Usuario já cadastrado')
            return redirect('cadastro')

        # escritorio = Escritorio.objects.create_user(
        #     username=usuario, nomeEscritorio=usuario, email=email, password=senha, senha=senha, qtdChaves=licencas, is_staff=False
        # )

        escritorio = Escritorio.objects.create_user(
            username=usuario, nomeEscritorio=usuario, email=email, password=senha, qtdChaves=licencas, is_staff=False
        )

        escritorio.save()

        print('2 - ', usuario, senha, confirmaSenha, email, licencas)
        print('Usuario cadastrado com Sucesso')

        return redirect('login')
    else:
        return render(request, 'cadastro.html')


def login(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        senha = request.POST['senha']

        if usuario == "" or senha == "":
            return redirect('login')

        print(usuario, senha)
        if Escritorio.objects.filter(nomeEscritorio=usuario).exists():
            nome = Escritorio.objects.filter(nomeEscritorio=usuario).values_list('nomeEscritorio', flat=True)

            escritorio = auth.authenticate(request, username=nome[0], password=senha)

            if escritorio is not None:
                auth.login(request, escritorio)
                print('login to dash ID ----', escritorio.escritorioId)

                return redirect('dashboard', escritorio.escritorioId)
                # return redirect('dashboard')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


def dashboard(request, nomeEscritorio):

    if request.user.is_authenticated:

        # escritorioOBJ = get_object_or_404(Escritorio, pk=escritorioId)
        # userAtivo = request.user.escritorioId

        idUsuarioAtual = request.user.escritorioId
        chavesTotais = request.user.qtdChaves
        advCadstrado = Advogado.objects.filter(escritorioId=idUsuarioAtual)

        chaves = {}
        dicioChaves = {}
        print('chaves T -------------------------------', chavesTotais)

        if Advogado.objects.filter(escritorioId=idUsuarioAtual).exists():
            # advCadstrado = Advogado.objects.filter(escritorioId=escritorioId).values_list('usuarioId', flat=True)
            print('***************************************************************')
            print(advCadstrado)
            print(advCadstrado[0])
            # print(advCadstrado[1])
            print(advCadstrado[0].nomeUsuario)
            print(advCadstrado[0].email)
            # dicioChaves = {'advogados': advCadstrado}'
            dicioChaves["advogados"] = advCadstrado

            print('-------------------------------------------', len(advCadstrado))
            for i in advCadstrado:
                print(i)

            # return render(request, 'dashboard.html', dicioChaves)

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
    escritorioAtivo = get_object_or_404(Escritorio, pk=request.user.escritorioId, nomeEscritorio=nomeEscritorio)
    escritorioAtivoEditar = {'escritorio': escritorioAtivo}
    return render(request, 'atualiza_Escritorio.html', escritorioAtivoEditar)


def atualizaEscritorio(request):
    if request.method == 'POST':
        pass
    return redirect('dashboard', request.user.nomeEscritorio)



def criaAdv(request):
    form = AdvForm(request.POST or None)

    if form.is_valid():

        novo = form.save(commit=False)
        novo.escritorioId = request.user
        novo.save()
        form.save()
        return redirect('dashboard', request.user.nomeEscritorio)

    return render(request, 'cadAdv.html', {'form': form})


def editaAdv(request, advogadoId):
    cardAdv = get_object_or_404(Advogado, pk=advogadoId)
    form = AdvForm(request.POST or None)
    cardAdvEditar = {'adv': cardAdv}
    return render(request, 'atualiza_adv.html', cardAdvEditar)


def atualizaAdv(request):
    if request.method == 'POST':
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

        update.save()

    return redirect('dashboard', request.user.nomeEscritorio)


def deletaAdv(request, advogadoId):
    cardAdv = get_object_or_404(Advogado, pk=advogadoId)
    cardAdv.delete()
    return redirect('dashboard', request.user.nomeEscritorio)

