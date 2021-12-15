from colorama import Fore, init, Back, deinit
import os
from datetime import datetime

from prevEnums import TipoLog, Prioridade
from utils.datetimeUtils import datetimeToStr


def logPrioridade(mensagem: str, tipoLog: TipoLog, priodiade: Prioridade = Prioridade.normal, verbose: bool = False):
    init(autoreset=True)

    if tipoLog == TipoLog.rest:
        path = os.path.join(os.getcwd(), 'logs', 'historicoLogs', f'{datetime.now().date()}-REST.txt')
        corDaFonte = Fore.YELLOW
    elif tipoLog == TipoLog.cache:
        path = os.path.join(os.getcwd(), 'logs', 'historicoLogs', f'{datetime.now().date()}-CACHE.txt')
        corDaFonte = Fore.MAGENTA
    elif tipoLog == TipoLog.sync:
        path = os.path.join(os.getcwd(), 'logs', 'historicoLogs', f'{datetime.now().date()}-SYNC.txt')
        corDaFonte = Fore.BLUE
    else:
        path = os.path.join(os.getcwd(), 'logs', 'historicoLogs', f'{datetime.now().date()}-BANCO.txt')
        corDaFonte = Fore.GREEN

    if priodiade == Prioridade.normal:
        corDoFundo = Back.RESET
    elif priodiade == Prioridade.warnings:
        corDoFundo = Back.YELLOW
        corDaFonte = Fore.LIGHTWHITE_EX
    elif priodiade == Prioridade.erro:
        corDoFundo = Back.RESET
        corDaFonte = Fore.LIGHTWHITE_EX

    with open(path, mode='a', encoding='utf-8') as log:
        log.write(datetimeToStr(datetime.now()) + ' -> ' + mensagem + '\n')
        log.flush()

    if verbose or tipoLog == TipoLog.erro:
        print(corDaFonte + corDoFundo + datetimeToStr(datetime.now()) + '----' + mensagem)

    deinit()

