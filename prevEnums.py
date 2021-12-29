from enum import Enum


class TipoConexao(Enum):
    magic = 1
    hearthstone = 2


class TipoLog(Enum):
    rest = 0
    cache = 1
    banco = 2
    sync = 3
    erro = 4


class Prioridade(Enum):
    normal = 0
    warnings = 1
    erro = 2
