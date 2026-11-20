def lire_entier(message, minimum, maximum):
    while True:
        texte = input(message)
        try:
            n = int(texte)
        except ValueError:
            print("Erreur : ce n'est pas un entier.")
            continue
        if n < minimum or n > maximum:
            print("Erreur : valeur hors limites (", minimum, "à", maximum, ").")
        else:
            return n


mois = lire_entier("Nombre de mois (1-360) : ", 1, 360)
print("Vous avez choisi", mois, "mois.")