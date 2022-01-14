# Programe par Eliot CASSIDY

def dich_search(values: list, arg) -> tuple[bool, int]:
    """ Recherche si arg in values et renvoie (True | False, Indice | -1)"""
    assert isinstance(values, list) and len(values) > 0 and not(isinstance(arg, str))
    bas, haut = 0, len(values) - 1
    while bas <= haut:
        mid = (bas + haut) // 2
        if arg == values[mid]:
            return (True, mid)
        elif arg > values[mid]:
            bas = mid + 1
        else:
            haut = mid - 1
    return (False, -1)