from django.contrib import admin
from .models import Indicadores, ExpectativaSobrevida, IndicesAtualizacaoMonetaria


class AdminIndicadores(admin.ModelAdmin):
    list_display = ['indicadorId', 'resumo', 'fonte']
    list_display_links = ['indicadorId', 'resumo']
    list_per_page = 15


class AdminExpSobrevida(admin.ModelAdmin):
    list_display = ['dataReferente', 'idade', 'expectativaSobrevida']
    list_display_links = ['dataReferente', 'idade', 'expectativaSobrevida']
    list_per_page = 10


class AdminIndicesAtuMonetaria(admin.ModelAdmin):
    list_display = ['dataReferente', 'dib', 'fator']
    list_display_links = ['dataReferente', 'dib', 'fator']
    list_per_page = 30


admin.site.register(Indicadores, AdminIndicadores)
admin.site.register(ExpectativaSobrevida, AdminExpSobrevida)
admin.site.register(IndicesAtualizacaoMonetaria, AdminIndicesAtuMonetaria)
