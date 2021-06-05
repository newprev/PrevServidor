from django.urls import path

from .views import *


urlpatterns = [
    path('', pages.index, name='index'),
    path('cadastro', cadastro, name='cadastro'),
    path('login', pages.login, name='login'),
    # path('id=<int:escritorioId>', pages.dashboard, name='dashboard'),
    path('escritorio=<str:nomeEscritorio>', pages.dashboard, name='dashboard'),
    path('logout', pages.logout, name='logout'),
    path('novoAdv', pages.criaAdv, name='criaAdv'),
    path('updateAdv/<int:id>/', pages.updateAdv, name='updateAdv'),
    path('deleteAdv/<int:id>/', pages.deleteAdv, name='deleteAdv')
]