def junta(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1[0] < l2[0]:
        return [l1[0]] + junta(l1[1:], l2)
    return [l2[0]] + junta(l1, l2[1:])
