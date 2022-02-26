def selection(values: list) -> list:
    """Retourne la liste trié par séléction dans l'odre croissant"""
    n = len(values)
    for i in range(n-1):
        id_min = i
        for j in range(i+1, n):
            if values[id_min] > values[j]:
                id_min = j
        if id_min != i:
            tmp = values[i]
            values[i] = values[id_min]
            values[id_min] = tmp
    return values