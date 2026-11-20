import csv

soldes = {}
nb_ignorees = 0

f = open("operations.csv", "r", encoding="utf-8")
lecteur = csv.reader(f, delimiter=";")
next(lecteur)
numero = 1  # l'en-tête est la ligne 1
for ligne in lecteur:
    numero = numero + 1
    date, compte, type_op, montant = ligne
    try:
        montant = int(montant)
    except ValueError:
        nb_ignorees = nb_ignorees + 1
        print("Ligne", numero, "ignorée (montant invalide)")
        continue
    if compte not in soldes:
        soldes[compte] = 0
    if type_op == "Dépôt":
        soldes[compte] = soldes[compte] + montant
    else:
        soldes[compte] = soldes[compte] - montant
f.close()

print("Lignes ignorées :", nb_ignorees)
for compte in sorted(soldes):
    print(compte, soldes[compte])

g = open("soldes.csv", "w", encoding="utf-8", newline="")
ecrivain = csv.writer(g, delimiter=";")
ecrivain.writerow(["compte", "solde"])
for compte in sorted(soldes):
    ecrivain.writerow([compte, soldes[compte]])
g.close()