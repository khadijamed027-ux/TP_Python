janvier = {"C01", "C02", "C03", "C05", "C08"}
fevrier = {"C02", "C03", "C04", "C08", "C09"}
mars = {"C01", "C03", "C08", "C09", "C10"}
 
print("Venus les 3 mois        :", sorted(janvier & fevrier & mars))
print("Venus au moins une fois :", sorted(janvier | fevrier | mars))
print("Nouveaux clients de mars:", sorted(mars - janvier - fevrier))
 