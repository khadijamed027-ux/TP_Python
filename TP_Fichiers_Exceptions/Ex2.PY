import csv

f = open("operations.csv", "r", encoding="utf-8")
lecteur = csv.reader(f, delimiter=";")


for ligne in lecteur:
    date = ligne[0]
    compte = ligne[1]
    type_op = ligne[2]
    montant = ligne[3]

    annee = date[0:4]
    mois = date[5:7]
    jour = date[8:10]

    

    print(jour + "/" + mois + "/" + annee, compte, type_op, montant)

f.close()