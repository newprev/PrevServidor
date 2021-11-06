from os import path
import os, django
from datetime import date, datetime
from typing import List
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PrevServidor.settings')
django.setup()

from django.db import models
from apps.informacoes.models import ExpectativaSobrevida

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


def convertToFloat(textoComNumero: str):
    strResultado: str = textoComNumero.replace(',', '.')
    return float(strResultado)


def main():
    pathArquivos = path.join(os.getcwd(), os.path.pardir, 'backup', 'expSobrevida')
    listaArquivos: List[str] = os.listdir(pathArquivos)
    allData: List[dict] = []
    listaModels: List[ExpectativaSobrevida] = []
    i: int = 0

    for arquivo in listaArquivos:
        sexo = arquivo[0]
        dataAno: str = date(year=int(arquivo[1:5]), month=1, day=1).strftime('%Y-%m-%d')

        df_Arquivo: pd.DataFrame = pd.read_csv(path.join(pathArquivos, arquivo))
        columns = ['idade', '-', '--', '---', '----', '-----', 'expectativaSobrevida']
        df_Arquivo.columns = columns
        df_queImporta = df_Arquivo[['idade', 'expectativaSobrevida']]
        df_queImporta['expectativaSobrevida'] = df_queImporta['expectativaSobrevida'].apply(convertToFloat)
        df_queImporta['genero'] = sexo
        df_queImporta['dataReferente'] = dataAno
        allData.extend(df_queImporta.to_dict(orient='records'))

        #
        #     indiceAtu = IndicesAtualizacaoMonetaria()
        #     indiceAtu.dataReferente = dataReferente
        #     indiceAtu.fator = fator
        #     indiceAtu.dib = nomeArquivo
        #     indiceAtu.save()
        #     i += 1

        # print(f'- nomeArquivo: {nomeArquivo.date()} - linhas: {i}')
    # print(f'Qtd de inserções: {i}')
    # listaModels = [ExpectativaSobrevida(**exp) for exp in allData]
    # ExpectativaSobrevida.objects.bulk_create(listaModels)

main()
