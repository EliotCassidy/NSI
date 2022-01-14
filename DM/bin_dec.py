# Programes par Eliot CASSIDY

def binary_to_decimal(binval: str) -> int:
    """ Renvoie la valeur décimal d'un binaire ou -1 si valeur incorect"""
    if not(isinstance(binval, str)):
        return -1
    for letter in range(len(binval)):
        if binval[letter] not in ["0", "1"]:
            return -1

    decval, k = 0, 0
    for i in range(len(binval) - 1, -1, -1):
        decval += int(binval[i]) * 2**k
        k += 1
    return decval



def decimal_to_binary(decval: int) -> str:
    """ Renvoie la valeur binaire d'un décimal ou -1 si valeur incorect"""
    if not(isinstance(decval, int)) or decval < 0:
        return "-1"
    if decval == 0:
        return "0"
    
    binval = ""
    while True:
        if decval == 0:
            break
        elif decval % 2 == 0:
            decval //= 2
            binval += "0"
        else:
            decval //= 2
            binval += "1"
    # Renvoie la valeur binval inversée
    return binval[::-1]