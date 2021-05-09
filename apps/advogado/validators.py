from validate_docbr import CPF


def validaCpf(numeroCpf: str):
    cpf = CPF()
    return cpf.validate(numeroCpf)


def validaTamanhoNumOAB(numeroOAB: str):
    return len(numeroOAB) == 9


def validaApenasNumerosOAB(numeroOAB: str):
    return numeroOAB.isdecimal()


def validaNomeUsuario(nomeUsuario: str):
    return nomeUsuario.isalpha()


def validaSobrenomeUsuario(sobrenomeUsuario: str):
    return sobrenomeUsuario.isalpha()
