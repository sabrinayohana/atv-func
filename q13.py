def inverter_lista(lista):
    if len(lista) <= 1:
        return lista
    return [lista[-1]] + inverter_lista(lista[:-1])
