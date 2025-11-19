def calculerRemise(total, clientFidele):
    """
    Calcule la remise sur le total d'achat.
    Si le client est fidèle, applique 10% de remise.
    Sinon, pas de remise.

    Args:
        total (float): Montant total de l'achat.
        clientFidele (bool): Indique si le client est fidèle.

    Returns:
        float: Montant après remise.

    Raises:
        ValueError: si le total est négatif.
    """
    if total < 0:
        raise ValueError("Le total ne peut pas être négatif")
    if clientFidele:
        return total * 0.9
    else:
        return total