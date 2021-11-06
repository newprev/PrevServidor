from typing import List
import pandas as pd
import openpyxl
import datetime


def timestampToDate(timestp: pd.Series) -> datetime.date:
    trf = lambda x: x.to_pydatetime().date()
    return timestp.apply(trf)


def carregaArquivo(path: str) -> pd.DataFrame:
    df: pd.DataFrame = pd.read_excel(path)
    df['dataValidade'] = timestampToDate(df['dataValidade'])
    return df


def main():
    path = '../../tetosPrev.xlsx'
    dfTetos: pd.DataFrame = carregaArquivo(path)
    dictTetos: List[dict] = dfTetos.to_dict(orient='records')
    strComando: str ="""
    INSERT INTO ferramentas_tetosprev 
	    (dataValidade, valor, dataUltAlt, dataCadastro)
    VALUE
    """

    for index, teto in enumerate(dictTetos):
        if index == 0:
            strComando += f"""('{teto['dataValidade']}', {teto['valor']}, NOW(), NOW())"""
        else:
            strComando += f""",\n('{teto['dataValidade']}', {teto['valor']}, NOW(), NOW())"""

    print(strComando)

main()

