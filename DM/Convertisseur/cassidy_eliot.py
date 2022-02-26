# Made by : Eliot CASSIDY
# Last updated : 28/01/2022
# Purpose : 3 fonctions qui servent à convertir des entiers naturelles en différentes bases
# Extra : Devoir Maison de NSI pour le 4 mars 2022




def decimal_a_binaire(decval: int) -> int:
    """Renvoie la valeur binaire d'un entier decimal positif"""
    
    # Assertion pour les cas interdits
    assert isinstance(decval, int) and decval >= 0
    if decval == 0:
        return 0

    # Binval prend la valeur binaire (inversée) de decval à la fin de la boucle while
    binval = ""
    while decval != 0:
        binval += str(decval % 2)
        decval //= 2
                    
    # Renvoie la valeur binval inversée
    reversed_binval = ""
    for i in range(len(binval)):
        reversed_binval = binval[i] + reversed_binval
    return int(reversed_binval)



def binaire_a_decimal(binval: int) -> int:
    """Renvoie la valeur décimal d'un binaire entier positif"""
    
    # Assertion pour les cas interdits
    assert isinstance(binval, int) and binval >= 0
    binval = str(binval)
    for letter in range(len(binval)):
        assert binval[letter] == "0" or binval[letter] == "1"

    # Decval prend la valeur décimal de binval à la fin de la boucle for
    decval, k = 0, 0
    for i in range(len(binval) - 1, -1, -1):
        decval += int(binval[i]) * 2**k
        k += 1
    return decval



def binaire_a_hexadecimal(binval: int) -> str:
    """Renvoie la valeur hexadécimal d'un binaire entier positif"""
    
    # Assertion pour les cas interdits
    assert isinstance(binval, int) and binval >= 0
    binval = str(binval)
    for letter in range(len(binval)):
        assert binval[letter] == "0" or binval[letter] == "1"
    
    # Définition du dictionnaire de conversion bin->hex
    lookup = {"0000" : "0", "0001" : "1", "0010" : "2", "0011" : "3", "0100" : "4",
              "0101" : "5", "0110" : "6", "0111" : "7", "1000" : "8", "1001" : "9",
              "1010" : "A", "1011" : "B", "1100" : "C", "1101" : "D", "1110" : "E",
              "1111" : "F"}
    
    # Ajout de 0 au début de binval pour grouper en paquet de 4
    while len(binval) % 4 != 0:
        binval = "0" + binval
    
    hexval = ""
    for i in range(0, len(binval) - 3, 4):
        key = binval[i] + binval[i + 1] + binval[i + 2] + binval[i + 3]
        hexval += lookup[key]
    return hexval




""" Programme principal"""

entier_decimal = 15
print("Entier décimal :", entier_decimal)

entier_binaire = decimal_a_binaire(entier_decimal)
print("Entier binaire :", entier_binaire)

entier_hexa = binaire_a_hexadecimal(entier_binaire)
print("Entier hexadécimal :", entier_hexa)

entier_binaire = 1111
print("Entier décimal :", binaire_a_decimal(entier_binaire))