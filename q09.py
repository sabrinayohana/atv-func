def soma_pares(lista):
    if not lista:
        return 0
    if lista[0] % 2 == 0:
        return lista[0] + soma_pares(lista[1:])
    return soma_pares(lista[1:])
