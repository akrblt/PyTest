import pytest
from calculer_remise import calculerRemise

# Test 1 : Cas standard - client fidèle
def test_client_fidele_remise_appliquee():
    # Arrange
    total = 100
    client_fidele = True

    # Act
    resultat = calculerRemise(total, client_fidele)

    # Assert
    assert resultat == 90.0

# Test 2 : Cas standard - client non fidèle
def test_client_non_fidele_aucune_remise():
    # Arrange
    total = 100
    client_fidele = False

    # Act
    resultat = calculerRemise(total, client_fidele)

    # Assert
    assert resultat == 100.0

# Test 3 : Cas limite - total égal à 0
def test_total_zero():
    # Arrange
    total = 0
    client_fidele = True

    # Act
    resultat = calculerRemise(total, client_fidele)

    # Assert
    assert resultat == 0.0

# Test 4 : Cas d'erreur - total négatif
def test_total_negatif_exception():
    # Arrange
    total = -50
    client_fidele = True

    # Act & Assert
    with pytest.raises(ValueError):
        calculerRemise(total, client_fidele)

# Test 5 : Format mixte - mauvais type
def test_type_invalide_chaine():
    with pytest.raises(TypeError):
        calculerRemise("100", True)
