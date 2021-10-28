from prevEnums import TipoConexao
import os
import json


def getDatabase(conexao: TipoConexao):
    if conexao == TipoConexao.magic:
        strPathSource: str = os.path.join(os.getcwd(), 'datasource', 'magic.json')
    elif conexao == TipoConexao.hearthstone:
        strPathSource: str = os.path.join(os.getcwd(), 'datasource', 'hearthstone.json')

        with open(strPathSource, encoding='utf-8', mode='r') as cacheLogin:
            banco = json.load(cacheLogin)

        return banco
