from django.contrib import admin
from .models import Advogado
from django.contrib.auth.mixins import LoginRequiredMixin


@admin.register(Advogado)
class AdminAdvogado(admin.ModelAdmin, LoginRequiredMixin):
    list_display = ['usuarioId', 'nomeUsuario', 'escritorioId', 'login', 'email', 'ativo', 'confirmado']
    list_display_links = ['usuarioId', 'escritorioId', 'login', 'email', 'nomeUsuario']
    list_filter = ['escritorioId',]
    list_editable = ['ativo', 'confirmado']
    readonly_fields = ['usuarioId', ]
    ordering = ['nomeUsuario', ]
    list_per_page = 15

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # form.base_fields["escritorioId"].label = "Escritorios:"
        return form

# admin.site.register(Advogado, AdminAdvogado)

