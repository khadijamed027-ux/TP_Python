ventes_v = [("Aicha", 12000), ("Sidi", 8000), ("Aicha", 15500),
            ("Mohamed", 4000), ("Sidi", 22000), ("Aicha", 3000),
            ("Fatimetou", 18000)]

nb_ventes = {}   
ca = {}

for nom, montant in ventes_v:
    nb_ventes[nom] = nb_ventes.get(nom, 0) + 1
    ca[nom] = ca.get(nom, 0) + montant

print("Nombre de ventes :", nb_ventes)
print("Chiffre d'affaires :", ca)