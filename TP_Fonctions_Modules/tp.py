"""Travaux pratiques – Chapitre V : Fonctions et modules."""


# ---------- Exercice 1 ----------
def maximum(a, b):
    """Renvoie le plus grand des deux nombres."""
    return a if a >= b else b


def est_pair(n):
    """Renvoie True si n est pair."""
    return n % 2 == 0


def moyenne(notes):
    """Moyenne d'une liste de notes, ou None si la liste est vide."""
    if not notes:
        return None
    return sum(notes) / len(notes)


# ---------- Exercice 2 ----------
def valeur_acquise(capital, taux, annees):
    """Valeur acquise avec intérêts composés (taux annuel en décimal)."""
    return capital * (1 + taux) ** annees


def mensualite(capital, taux_annuel, mois):
    """Mensualité constante d'un prêt amorti (taux mensuel = taux_annuel / 12)."""
    t = taux_annuel / 12
    if t == 0:
        return capital / mois
    return capital * t / (1 - (1 + t) ** (-mois))


def cout_credit(capital, taux_annuel, mois):
    """Total des intérêts payés sur la durée du prêt."""
    return mensualite(capital, taux_annuel, mois) * mois - capital


# ---------- Exercice 3 ----------
def facturer(lignes, catalogue, remise=0.0, tva=0.16):
    """Calcule brut, remise, net HT, TVA et TTC d'une commande."""
    brut = 0
    for ref, qte in lignes:
        if ref not in catalogue:
            raise KeyError("Référence inconnue")
        brut += qte * catalogue[ref]
    montant_remise = brut * remise
    net_ht = brut - montant_remise
    montant_tva = net_ht * tva
    return {"brut": brut, "remise": montant_remise, "net_ht": net_ht,
            "tva": montant_tva, "ttc": net_ht + montant_tva}


if __name__ == "__main__":
    print(maximum(3, 8), est_pair(7), moyenne([12, 15, 9]), moyenne([]))
    for m in (12, 24, 36):
        print(m, "mois :", round(mensualite(500000, 0.12, m), 2),
              round(cout_credit(500000, 0.12, m), 2))
    cat = {"P01": 45000, "P02": 12000, "P03": 6500}
    print(facturer([("P01", 2), ("P03", 4)], cat, 0.05))
    try:
        facturer([("P99", 1)], cat)
    except KeyError as e:
        print("Erreur :", e)