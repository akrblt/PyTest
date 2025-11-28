


def calculerPrixAvecemise(totalHT,remise):
    if not isinstance(totalHT,(int,float)) or not isinstance(remise,(int,float)):
        raise TypeError("totalHT et remise doivernt etre numerique")
    if remise <0 or remise> 100:
        raise ValueError("remise dois etre entre 0 et 100")
    return totalHT *(1-remise/100)