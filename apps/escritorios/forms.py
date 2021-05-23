from django import forms
from apps.advogado.models import Advogado
from apps.escritorios.models import Escritorio
from apps.escritorios.models import Escritorio
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.conf import settings


# class AdvForm(forms.UserChangeForm):
# class AdvForm(forms.Form):
class AdvForm(forms.ModelForm):

    class Meta:
        model = Advogado
        # exclude = ('escritorioId',)

        # fields = ["escritorioId", "nomeUsuario", "sobrenomeUsuario", "numeroOAB",
        #           "login", "senha", "email","nacionalidade", "estadoCivil", "ativo", ]

        # fields = "__all__"

        fields = ["nomeUsuario", "sobrenomeUsuario", "numeroOAB",
        "login", "senha", "email","nacionalidade", "estadoCivil", "ativo", ]

        labels = {
            # "escritorioId": "Escritório",
            "nomeUsuario": "Nome",
            "sobrenomeUsuario": "Sobre Nome",
            "numeroOAB": "Nº OAB"
        }

    # escritorioId = forms.DateField(label="Id", disabled=True, initial='auth.User')
    # escritorioId = forms.DateField(label="Id", disabled=True, initial=Escritorio.escritorioId)
    # escritorioId = forms.DateField(label="Id", disabled=True)
    # escritorioId = forms.ModelChoiceField(queryset=Escritorio.objects.all(), empty_label="(Nothing)", to_field_name='escritorioId', initial=settings.AUTH_USER_MODEL)
    # escritorioId = forms.ModelChoiceField(queryset=Escritorio.objects.none())
