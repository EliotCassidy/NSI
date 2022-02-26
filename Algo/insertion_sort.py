def insertion(values: list, reverse: bool = False) -> list:
    """Retourne la liste trié par insertion dans l'odre croissant ou décroissant si indiqué"""
    assert isinstance(values, list)
    for i in range(1, len(values)):
        key = values[i]
        j = i
        if not(reverse):
            while values[j - 1] > key and j > 0:
                values[j] = values[j - 1]
                j -= 1
        else:
            while values[j - 1] < key and j > 0:
                values[j] = values[j - 1]
                j -= 1

        values[j] = key
    return values
