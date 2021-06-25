def dashCards(qtdLicenca):
    chaves = {}
    for chave in range(1, qtdLicenca + 1):
        chaves[chaves] = chave
    dicioChaves = {'dados': chaves}
    return dicioChaves


def campoVazio(campo):
    return not campo.strip()


def senhasIguais(senha1, senha2):
    return senha1 != senha2