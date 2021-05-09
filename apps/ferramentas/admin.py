from django.contrib import admin
from .models import ConvMon, TetosPrev

class AdminConvMon(admin.ModelAdmin):
    list_display = ['convMonId', 'nomeMoeda', ]
    list_display_links = ['convMonId', 'nomeMoeda', ]
    search_fields = ['dataInicial', 'dataFinal']

admin.site.register(ConvMon, AdminConvMon)


class AdminTetosPrev(admin.ModelAdmin):
    list_display = ['tetosPrevId', 'dataValidade', 'valor']
    list_display_links = ['tetosPrevId', 'dataValidade', 'valor']
    search_fields = ['dataValidade', 'valor']
    list_per_page = 20

admin.site.register(TetosPrev, AdminTetosPrev)