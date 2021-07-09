from django.contrib import admin
from .models import Indicadores, ExpectativaSobrevida


class AdminIndicadores(admin.ModelAdmin):
    list_display = ['indicadorId', 'resumo', 'fonte']
    list_display_links = ['indicadorId', 'resumo']
    list_per_page = 15


class AdminExpSobrevida(admin.ModelAdmin):
    list_display = ['dataReferente', 'idade', 'expectativaSobrevida']
    list_display_links = ['dataReferente', 'idade', 'expectativaSobrevida']
    list_per_page = 10


admin.site.register(Indicadores, AdminIndicadores)
admin.site.register(ExpectativaSobrevida, AdminExpSobrevida)
