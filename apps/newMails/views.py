from apps.escritorios.models import Escritorio
from apps.advogado.models import Advogado
from logs.logRest import logPrioridade

from django.core.mail import send_mail

from prevEnums import TipoLog, Prioridade


def emailBoasVindas(escritorio: Escritorio) -> True:
    try:
        send_mail(
            f'Seja bem vindo(a), {escritorio.nomeFantasia}',
            f'Olá!\nÉ um prazer ter você conosco. Abaixo estão alguns dos seus dados. Pedimos que confirme-os e, se tudo estiver correto, é só acessar nossa plataforma e '
            f'cadastrar os advogados que trabalharão na {escritorio.nomeFantasia}!',
            'thomas.anderson@newprev.dev.br',
            [escritorio.email],
            fail_silently=False
        )
        logPrioridade("E-mail::emailBoasVindas", tipoLog=TipoLog.rest)
        return True
    except Exception as err:
        print(f"apps/newMail/views/cadastro: {err}")
        logPrioridade(f"E-mail::emailBoasVindas::{err}", tipoLog=TipoLog.rest, priodiade=Prioridade.erro)
        return False


def primeiroAcessoAdvogado(advogado: Advogado) -> True:
    return True