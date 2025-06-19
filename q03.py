def f(x, y):
    if x >= y:
        return (x + y) / 2
    else:
        return f(f(x + 2, y - 1), f(x + 1, y - 2))


# (a):
# f(1,8)
# ├── f(f(3,7), f(2,6))
#     ├── f(3,7)
#     │   ├── f(f(5,6), f(4,5))
#     └── f(2,6)
#         ├── f(f(4,5), f(3,4))
# a árvore continua até os valores de x serem maiores ou iguais a y

# (b):
# No fim das contas, a função retorna 5.0
# ela vai fazendo várias médias até chegar nesse valor

# (c):
# Ela basicamente tenta encontrar um valor "meio termo" entre x e y,
# usando chamadas recursivas que fazem x aumentar e y diminuir.
# Quando x fica maior ou igual a y, ela para e devolve a média dos dois.
# É como se fosse uma espécie de média adaptativa ou "equilíbrio" entre x e y.

