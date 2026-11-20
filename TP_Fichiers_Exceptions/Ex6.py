def virement(soldes, source, destination, montant):
    if source not in soldes or destination not in soldes:
        raise KeyError("Compte inexistant")
    if montant <= 0:
        raise ValueError("Le montant doit être positif")
    if soldes[source] < montant:
        raise ValueError("Solde insuffisant")
    soldes[source] = soldes[source] - montant
    soldes[destination] = soldes[destination] + montant


soldes = {"CC-001": 33000, "CC-002": 37000, "CC-003": 8000}

tests = [("CC-001", "CC-002", 10000),
         ("CC-001", "CC-002", -5),
         ("CC-003", "CC-001", 50000),
         ("CC-001", "CC-999", 100)]

for source, destination, montant in tests:
    try:
        virement(soldes, source, destination, montant)
        print("Virement de", montant, "réussi :", soldes)
    except KeyError as e:
        print("Erreur de compte :", e)
    except ValueError as e:
        print("Erreur de montant :", e)