from django.contrib import admin
from .models import Advogado

class AdminAdvogado(admin.ModelAdmin):
    list_display = ['advogadoId', 'nomeUsuario', 'escritorioId', 'login', 'email', 'ativo', 'confirmado']
    list_display_links = ['advogadoId', 'escritorioId', 'login', 'email', 'nomeUsuario']
    list_filter = ['escritorioId',]
    list_editable = ['ativo', 'confirmado']
    readonly_fields = ['advogadoId', ]
    ordering = ['nomeUsuario', ]
    list_per_page = 15

admin.site.register(Advogado, AdminAdvogado)

