from django import forms
from apps.advogado.models import Advogado


class AdvForm(forms.ModelForm):
    class Meta:
        model = Advogado
        fields = ["escritorioId", "nomeUsuario", "sobrenomeUsuario", "numeroOAB",
                  "login", "senha", "email","nacionalidade", "estadoCivil", "ativo", ]

