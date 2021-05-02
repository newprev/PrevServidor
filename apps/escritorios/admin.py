from django.contrib import admin
from .models import Escritorio


class AdminEscritorio(admin.ModelAdmin):
    list_display = ['id', 'nomeFantasia', 'cnpj', 'cpf', 'ativo']
    list_display_links = ['id', 'nomeFantasia', 'cnpj', 'cpf']
    list_per_page = 15

    list_editable = ['ativo',]

admin.site.register(Escritorio, AdminEscritorio)