from django.urls import path

from .views import *


urlpatterns = [
    path('', pages.index, name='index'),
    path('cadastro', cadastro, name='cadastro'),
    path('login', pages.login, name='login'),
    path('dashboard', pages.dashboard, name='dashboard'),
]