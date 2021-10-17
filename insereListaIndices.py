from os import path
import os, django
from datetime import date, datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PrevServidor.settings')
django.setup()

from django.db import models
from apps.informacoes.models import IndicesAtualizacaoMonetaria

meses = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

def carregaArquivo(path: str):
    with open(path, mode='r') as f:
        linhas = f.readlines()
        return (l[1:] if l[0] == ',' else l[:] for l in linhas)


def avaliaInfo(data: str, tipo: str):
    if tipo == 'nomeArquivo':
        return datetime.strptime(data, '%Y-%m')
    elif tipo == 'fator':
        return float(data.replace(',', '.'))
    elif tipo == 'dataReferente':
        if data[0].isdigit():
            return datetime.strptime(data, '%m/%y')
        else:
            for chave, valor in meses.items():
                if valor.lower()[:3] == data[:3]:
                    mes = f"{chave}"
                    if len(mes) == 1:
                        mes = '0' + mes
                    return datetime.strptime(f"{mes}/{data[4:]}", '%m/%y')




def main():
    pathArquivos = path.join(os.getcwd(), os.path.pardir, 'Documentos', 'indicesAtualizacao')
    listaArquivos = os.listdir(pathArquivos)
    i: int = 0

    for arquivo in listaArquivos:
        linhas = carregaArquivo(path.join(pathArquivos, arquivo))
        nomeArquivo: datetime = avaliaInfo(arquivo[:len(arquivo) - 4], 'nomeArquivo')
        for f in linhas:
            dataReferente = avaliaInfo(f[:f.find(',')], 'dataReferente')

            fator = avaliaInfo(f[f.find('"')+1:f.rfind('"')], 'fator')
            # print(f"{nomeArquivo} - {dataReferente} - {fator}")

            indiceAtu = IndicesAtualizacaoMonetaria()
            indiceAtu.dataReferente = dataReferente
            indiceAtu.fator = fator
            indiceAtu.dib = nomeArquivo
            indiceAtu.save()
            i += 1

        # print(f'- nomeArquivo: {nomeArquivo.date()} - linhas: {i}')
    print(f'Qtd de inserções: {i}')

main()
