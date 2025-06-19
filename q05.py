def conta_bits(n):
    if n < 2:
        return 1
    return 1 + conta_bits(n // 2)
