def ordenada(lista):
    if len(lista) <= 1:
        return True
    if lista[0] > lista[1]:
        return False
    return ordenada(lista[1:])
