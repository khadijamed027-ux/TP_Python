montants = [1200, -350, 4800, 0, 15000, -90, 700]
 
positifs = [m for m in montants if m > 0]
absolus = [abs(m) for m in montants]
avec_tva = [round(m * 1.16) for m in montants if m > 0]
 
print("a) Positifs      :", positifs)
print("b) Valeurs abs.  :", absolus)
print("c) Positifs+TVA  :", avec_tva)
 