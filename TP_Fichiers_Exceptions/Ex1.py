#Question 1
f = open("produits.txt", "w", encoding="utf-8")
for i in range(5):
    designation = input("Désignation : ")
    prix = input("Prix : ")
    f.write(designation + ";" + prix + "\n")
f.close()
#Question 2
f = open("produits.txt", "r", encoding="utf-8")
lignes = f.readlines()
f.close()

total = 0
for ligne in lignes:
    morceaux = ligne.strip().split(";")
    designation = morceaux[0]
    prix = float(morceaux[1])
    print(designation.ljust(15), prix)
    total = total + prix

print("Prix moyen :", total / len(lignes))