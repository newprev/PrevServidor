from django.contrib import admin
from .models import Indicadores


class AdminIndicadores(admin.ModelAdmin):
    list_display = ['indicadorId', 'resumo', 'fonte']
    list_display_links = ['indicadorId', 'resumo']
    list_per_page = 15


admin.site.register(Indicadores, AdminIndicadores)
