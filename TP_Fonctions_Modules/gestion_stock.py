SEUIL_ALERTE = 10


def valeur_stock(stock, prix):
    total = 0
    for produit, quantite in stock.items():
        total = total + quantite * prix[produit]
    return total


def ruptures(stock, seuil=SEUIL_ALERTE):
    """Liste triée des références dont la quantité est inférieure au seuil."""
    return sorted(ref for ref, qte in stock.items() if qte < seuil)


def reapprovisionner(stock, ref, quantite):
    """Ajoute la quantité au stock de la référence et renvoie la nouvelle quantité."""
    stock[ref] = stock.get(ref, 0) + quantite
    return stock[ref]

