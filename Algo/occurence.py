# Programe par Eliot CASSIDY

def occurence(values: list, arg) -> bool:
    """Renvoie True si arg dans values ou False sinon"""
    assert isinstance(values, list)

    for i in range(len(values)):
        if values[i] == arg:
            return True
    return False