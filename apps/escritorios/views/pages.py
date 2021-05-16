from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import auth

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

        # if Escritorio.objects.filter(nomeEscritorio=usuario).exists():
        #     print('Nome de Usuario já cadastrado')
        #     return redirect('cadastro')

        # Cadastro do Escritório
        escritorio = Escritorio(nomeEscritorio=usuario, email=email, senha=senha, qtdChaves=licencas)
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

        if Escritorio.objects.filter(nomeEscritorio=usuario, senha=senha).exists():
            print(' Acesso Permitido ')
            escritorio = get_object_or_404(Escritorio, nomeEscritorio=usuario, senha=senha)
            print('-->  ')
            print('login 1 --->', escritorio.nomeEscritorio)
            print('login 1 --->', escritorio.escritorioId)
            return redirect('dashboard')
        else:
            print(' Acesso Não Permitido ')
            return redirect('login')
    return render(request, 'login.html')


def dashboard(request):

    escritorio = Escritorio.objects.all()
    infos = {
        "dados": escritorio
    }

    return render(request, 'dashboard.html', infos)
