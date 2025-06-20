def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos(lista):
    if not lista:
        return []
    if primo(lista[0]):
        return [lista[0]] + primos(lista[1:])
    return primos(lista[1:])
