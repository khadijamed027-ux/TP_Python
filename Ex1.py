print("Question 1:")
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
ventes = [125000, 98000, 143500, 87000, 210000, 176500]
Somme = sum(ventes)
Moyenne = Somme / len(ventes)
print("Le total est :", Somme, "et la moyenne est :", Moyenne)
print("Question 2:")
Max = max(ventes)
print(Max)
print("Le jour ou les ventes ont ete les plus fortes est :", jours[ventes.index(max(ventes))])
print("Question 3:")
print("Les jours deppassent la moyenne sont :")
for i in range(len(ventes)):
    if(ventes[i]>Moyenne):
        print(jours[i])
print("Question 4:")
couple=[]
for i in range(len(ventes)):
    couple.append((ventes[i],jours[i]))
couple.sort(reverse=True)
for i in range(len(couple)):
    print(couple[i][1], couple[i][0])    
