from django.contrib import admin
from .models import Advogado

class AdminAdvogado(admin.ModelAdmin):
    list_display = ['usuarioId', 'nomeUsuario', 'escritorioId', 'login', 'email', 'ativo']
    list_display_links = ['usuarioId', 'escritorioId', 'login', 'email', 'nomeUsuario']
    list_editable = ['ativo']
    readonly_fields = ['usuarioId', ]
    ordering = ['nomeUsuario', ]
    list_per_page = 15

admin.site.register(Advogado, AdminAdvogado)

