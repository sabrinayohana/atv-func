def divisores(n, k=1):
    if k > n:
        return []
    if n % k == 0:
        return [k] + divisores(n, k + 1)
    else:
        return divisores(n, k + 1)
