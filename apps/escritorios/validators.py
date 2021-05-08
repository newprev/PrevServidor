from validate_docbr import CPF, CNPJ


def validaCpf(numeroCpf: str):
    cpf = CPF()
    return cpf.validate(numeroCpf)


def validaCNPJ(numeroCNPJ: str):
    cnpj = CNPJ()
    return cnpj.validate(numeroCNPJ)

