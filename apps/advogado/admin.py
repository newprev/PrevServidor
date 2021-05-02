from django.contrib import admin
from .models import Advogado

class AdminAdvogado(admin.ModelAdmin):
    list_display = ['id', 'nomeUsuario', 'escritorioId', 'login', 'email', 'ativo']
    list_display_links = ['id', 'escritorioId', 'login', 'email', 'nomeUsuario']
    list_per_page = 15
    list_editable = ['ativo']

admin.site.register(Advogado, AdminAdvogado)

