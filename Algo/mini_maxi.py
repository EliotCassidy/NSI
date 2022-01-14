# Programe par Eliot CASSIDY

def mini_maxi(values: list) -> tuple[int, int]:
    """Renvoie les extremums de la liste => tuple(mini, maxi)"""
    assert isinstance(values, list) and len(values) > 0
    mini, maxi = 0, 0
    for i in range(len(values)):
        if values[i] > values[maxi]:
            maxi = i
        elif values[i] < values[mini]:
            mini = i
    return (values[mini], values[maxi])