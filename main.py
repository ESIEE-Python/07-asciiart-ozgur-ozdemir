"""
07 asciiart-ozgur-ozdemir
"""

#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici

    if not s:  # Si la chaîne est vide
        return []

    result = []
    current_char = s[0]  # Premier caractère
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))  # Ajout du tuple
            current_char = char
            count = 1

    result.append((current_char, count))

    return result


def artcode_r(s):
    """retourne la liste de tuples encodant une cdc passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici

    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif
    if not s:
        return []

    result = []
    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1

    result.append((current_char, count))
    return result

#### Fonction principale


def main():
    """ fonction principale"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
