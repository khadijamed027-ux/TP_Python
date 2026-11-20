import gestion_stock as gs

stock = {"P01": 4, "P02": 15, "P03": 8, "P04": 120}
prix = {"P01": 45000, "P02": 12000, "P03": 6500, "P04": 350}

print("Valeur du stock :", gs.valeur_stock(stock, prix))
print("Ruptures (seuil 10) :", gs.ruptures(stock))
print("Ruptures (seuil 5) :", gs.ruptures(stock, 5))
print("Nouvelle quantité P01 :", gs.reapprovisionner(stock, "P01", 20))
print("Ruptures après réappro :", gs.ruptures(stock))