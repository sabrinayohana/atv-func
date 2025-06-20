def ocorrencias(lista, x):
    if not lista:
        return 0
    if lista[0] == x:
        return 1 + ocorrencias(lista[1:], x)
    return ocorrencias(lista[1:], x)
