import threading
import requests as http
from datetime import datetime, date
from apps.informacoes.models import IpcaMensal


def atualizaMensalmente(evento: threading.Event):
    if not evento.is_set():
        sincronizaTabelaIpca()
        threading.Timer(4, atualizaMensalmente, [evento]).start()


def sincronizaTabelaIpca():
    apiPath: str = 'https://servicodados.ibge.gov.br/api/v3/agregados/6691/periodos/201411|201412|201501|201502|201503|201504|201505|201506|201507|201508|201509|201510|201511|201512|201601|201602|201603|201604|201605|201606|201607|201608|201609|201610|201611|201612|201701|201702|201703|201704|201705|201706|201707|201708|201709|201710|201711|201712|201801|201802|201803|201804|201805|201806|201807|201808|201809|201810|201811|201812|201901|201902|201903|201904|201905|201906|201907|201908|201909|201910|201911|201912|202001|202002|202003|202004|202005|202006|202007|202008|202009|202010|202011|202012|202101|202102|202103|202104|202105|202106|202107|202108|202109/variaveis/63?localidades=N1[all]'
    try:
        jsonIndices: dict = http.get(apiPath).json()[0]['resultados'][0]['series'][0]['serie']
        for data, valor in jsonIndices.items():
            dataRecebida = datetime.strptime(data, '%Y%m').date()
            valorRecebido = float(valor)

            indice = IpcaMensal.objects.get(dataReferente=dataRecebida, valor=valorRecebido)
            print(indice)


            # indice.dataReferente = datetime.strptime(data, '%Y%m').date()
            # indice.save()
    except Exception as err:
        print(err)

def servicosSync():
    evento = threading.Event()
    atualizaMensalmente(evento)

    # 2.630.000 segundos = 30 dias
    # mensal = scheduler(atualizaMensalmente, sleep(2630000))
    # mensal.enter(2630000, 1, atualizaMensalmente)
    # agendaMensal.enter(2, 2, atualizaMensalmente)
    # agendaMensal.run(blocking=False)