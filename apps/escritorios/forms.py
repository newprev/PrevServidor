from django import forms
from apps.advogado.models import Advogado


class AdvForm(forms.ModelForm):

    class Meta:
        model = Advogado
        # exclude = ('escritorioId',)

        # fields = ["escritorioId", "nomeUsuario", "sobrenomeUsuario", "numeroOAB",
        #           "login", "senha", "email","nacionalidade", "estadoCivil", "ativo", ]

        # fields = "__all__"

        fields = [
            "nomeUsuario",
            "sobrenomeUsuario",
            "numeroOAB",
            "login",
            "email",
            "nacionalidade",
            "estadoCivil",
            "ativo"
        ]

        labels = {
            "nomeUsuario": "Nome",
            "sobrenomeUsuario": "Sobre Nome",
            "numeroOAB": "Nº OAB"
        }

        widgets = {
            'nomeUsuario': forms.TextInput(attrs={'class': 'form__campo'}),
            'sobrenomeUsuario': forms.TextInput(attrs={'class': 'form__campo'}),
            'numeroOAB': forms.TextInput(attrs={'class': 'form__campo'}),
            'login': forms.TextInput(attrs={'class': 'form__campo'}),
            'email': forms.TextInput(attrs={'class': 'form__campo'}),
            'nacionalidade': forms.TextInput(attrs={'class': 'form__campo'}),
            'estadoCivil': forms.TextInput(attrs={'class': 'form__campo'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form__campo'}),
        }

    # escritorioId = forms.DateField(label="Id", disabled=True, initial='auth.User')
    # escritorioId = forms.DateField(label="Id", disabled=True, initial=Escritorio.escritorioId)
    # escritorioId = forms.DateField(label="Id", disabled=True)
    # escritorioId = forms.ModelChoiceField(queryset=Escritorio.objects.all(), empty_label="(Nothing)", to_field_name='escritorioId', initial=settings.AUTH_USER_MODEL)
    # escritorioId = forms.ModelChoiceField(queryset=Escritorio.objects.none())
