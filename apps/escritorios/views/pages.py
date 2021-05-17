from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import auth

from apps.escritorios.views.dashTools import *

from django.http import HttpResponse

# Create your views here.
from apps.escritorios.models import Escritorio


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

        print('login 1 -->', usuario, senha)

        if Escritorio.objects.filter(nomeEscritorio=usuario).exists():
            nome = Escritorio.objects.filter(nomeEscritorio=usuario).values_list('nomeEscritorio', flat=True)
            print('login 2 -->', nome[0])

            escritorio = auth.authenticate(request, username=nome[0], password=senha)

            print('login 3  -->', escritorio.email)

            if escritorio is not None:
                auth.login(request, escritorio)
                print('login to dash ID ----', escritorio.escritorioId)

                return redirect('dashboard', escritorio.escritorioId)
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


def dashboard(request, escritorioId):

    if request.user.is_authenticated:

        escritorioOBJ = get_object_or_404(Escritorio, pk=escritorioId)
        print('teste -------------', escritorioOBJ.email)

        chaves = {}
        for chave in range(1, escritorioOBJ.qtdChaves + 1):
            chaves[chave] = chave

        dicioChaves = {'dados': chaves}

        print(dicioChaves)

        # testeGet = get_object_or_404(Escritorio, Escritorio.escritorioId)
        # print(testeGet.email)

        return render(request, 'dashboard.html', dicioChaves)
    return redirect('index')

