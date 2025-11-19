# test_recherche.py
import pytest

# Fonction fictive à tester
def rechercher_utilisateur(nom, base_donnees):
    """Recherche un utilisateur par nom dans une base de données simulée."""
    if not isinstance(nom, str):
        raise TypeError("Le nom doit être une chaîne de caractères.")
    if len(nom) == 0:
        raise ValueError("Le nom ne peut pas être vide.")
    return [u for u in base_donnees if nom.lower() in u.lower()]

# Base de données simulée
BASE_DONNEES = ["Alice", "Bob", "Charlie", "David"]

# Tests
def test_recherche_valide():
    result = rechercher_utilisateur("Bob", BASE_DONNEES)
    assert result == ["Bob"]

def test_recherche_partielle():
    result = rechercher_utilisateur("a", BASE_DONNEES)
    assert set(result) == set(["Alice", "Charlie", "David"])

def test_recherche_nom_vide():
    with pytest.raises(ValueError):
        rechercher_utilisateur("", BASE_DONNEES)

def test_recherche_type_invalide():
    with pytest.raises(TypeError):
        rechercher_utilisateur(123, BASE_DONNEES)

def test_recherche_non_trouve():
    result = rechercher_utilisateur("Zelda", BASE_DONNEES)
    assert result == []

def test_recherche_case_sensible():
    result = rechercher_utilisateur("CHARLIE", BASE_DONNEES)
    assert result == ["Charlie"]

# Test volontairement erroné pour l'exercice
def test_erreur_volontaire():
    result = rechercher_utilisateur("Bob", BASE_DONNEES)
    # Erreur dans la valeur attendue : "Bob" est en majuscule, on met volontairement "bob"
    assert result == ["Bob"]