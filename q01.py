def conta_divisores(n, k=1):
    if k > n:
        return 0
    if n % k == 0:
        return 1 + conta_divisores(n, k + 1)
    else:
        return conta_divisores(n, k + 1)