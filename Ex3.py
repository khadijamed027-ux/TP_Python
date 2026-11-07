print("Question a :")
catalogue = {
"P01": {"nom": "Ordinateur portable", "categorie": "Informatique",
"prix": 45000},
"P02": {"nom": "Imprimante", "categorie": "Informatique",
"prix": 12000},
"P03": {"nom": "Chaise de bureau", "categorie": "Mobilier",
"prix": 6500},
"P04": {"nom": "Ramette papier", "categorie": "Fournitures",
"prix": 350},
}
catalogue["P05":]={"nom": "Bureau", "categorie": "Mobilier", "prix": 45000}
print(catalogue)
print("Question b :")
for i in catalogue:
    if catalogue[i]["categorie"] == "Informatique":
        catalogue[i]["prix"]=catalogue[i]["prix"]*1.05
        print(catalogue)
print("Question c :")
del catalogue ["P04"]      
print(catalogue)
print("Question e :")
somme_cat = {}
nb_cat = {}
for p in catalogue.values():
    cat = p["categorie"]
    somme_cat[cat] = somme_cat.get(cat, 0) + p["prix"]
    nb_cat[cat] = nb_cat.get(cat, 0) + 1
print("\nPrix moyen par catégorie :")
for cat in somme_cat:
    print(f"  {cat:<14} {somme_cat[cat] / nb_cat[cat]:>10.2f}")

    

