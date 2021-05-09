from django.contrib import admin
from .models import Advogado

class AdminAdvogado(admin.ModelAdmin):
    list_display = ['usuarioId', 'nomeUsuario', 'escritorioId', 'login', 'email', 'ativo', 'confirmado']
    list_display_links = ['usuarioId', 'escritorioId', 'login', 'email', 'nomeUsuario']
    list_filter = ['escritorioId',]
    list_editable = ['ativo', 'confirmado']
    readonly_fields = ['usuarioId', ]
    ordering = ['nomeUsuario', ]
    list_per_page = 15

admin.site.register(Advogado, AdminAdvogado)

