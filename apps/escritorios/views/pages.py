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

        # Validação de email
        if not email.strip():
            print('O Email  não pode ficar em branco')
            return redirect('cadastro')

        # Validação de senha
        if senha != confirmaSenha:
            print('As senhas digitadas não são iguais')
            return redirect('cadastro')

        # Validação de usuário existente no banco
        if Escritorio.objects.filter(email=email, nomeEscritorio=usuario).exists():
            print('Email Usuario já cadastrado')
            return redirect('cadastro')

        escritorio = Escritorio.objects.create_superuser(
            username=usuario, nomeEscritorio=usuario, email=email, password=senha, senha=senha, qtdChaves=licencas
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
        teste = {}

        if Advogado.objects.filter(escritorioId=idUsuarioAtual).exists():
            # advCadstrado = Advogado.objects.filter(escritorioId=escritorioId).values_list('usuarioId', flat=True)
            print('***************************************************************')
            print(advCadstrado)
            print(advCadstrado[0])
            # print(advCadstrado[1])
            print(advCadstrado[0].nomeUsuario)
            print(advCadstrado[0].email)
            dicioChaves = {'advogados': advCadstrado}

            x = {'teste': {1: 1, 2: 2}}

            return render(request, 'dashboard.html', dicioChaves)

        for chave in range(1, chavesTotais + 1):
            if chave <= len(advCadstrado):
                chaves[chave] = advCadstrado[chave - 1]
            else:
                chaves[chave] = chave

        dicioChaves = {'advogados': chaves}
        return render(request, 'dashboard.html', dicioChaves)
    return redirect('index')

def criaAdv(request):
    form = AdvForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard', request.user.escritorioId)

    return render(request, 'cadAdv.html', {'form': form})
