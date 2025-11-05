def calculer_prix_ttc(prix_ht, tva):
    """
    Calcule le prix TTC à partir du prix HT et du taux de TVA.

    Args:
        prix_ht (float): prix hors taxe
        tva (float): taux de TVA (ex: 0.2 pour 20%)

    Returns:
        float: prix TTC

    Raises:
        ValueError: si prix_ht ou tva sont négatifs
        TypeError: si les types ne sont pas numériques
    """
    if not isinstance(prix_ht, (int, float)) or not isinstance(tva, (int, float)):
        raise TypeError("prix_ht et tva doivent être des nombres")
    if prix_ht < 0 or tva < 0:
        raise ValueError("prix_ht et tva doivent être positifs")
    return round(prix_ht * (1 + tva), 2)