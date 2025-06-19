def primo(n, k=2):
    if n < 2:
        return False
    if k * k > n:
        return True
    if n % k == 0:
        return False
    return primo(n, k + 1)
