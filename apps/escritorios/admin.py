from django.contrib import admin
from .models import Escritorio


class AdminEscritorio(admin.ModelAdmin):
    list_display = ['escritorioId', 'nomeFantasia', 'cnpj', 'cpf', 'ativo']
    list_display_links = ['escritorioId', 'nomeFantasia', 'cnpj', 'cpf']
    list_per_page = 15
    readonly_fields = ['escritorioId', ]

    list_editable = ['ativo',]

admin.site.register(Escritorio, AdminEscritorio)