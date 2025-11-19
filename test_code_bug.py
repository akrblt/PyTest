# test_code_bug.py
import pytest
from code_bug import ajouter, est_adulte, division,multiplier

def test_ajouter():
    assert ajouter(2, 3) == 5  # Devrait passer si fonction ok

def test_est_adulte_vrai():
    assert est_adulte(18) is True  # Test incorrect : 18 ans doit être adulte

def test_est_adulte_faux():
    assert est_adulte(17) is False

def test_division():
    assert division(10, 2) == 5

def test_division_par_zero():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)

def test_multiplier():
    # Test d'une fonction qui n'existe pas (erreur à corriger)
    assert multiplier(2, 3) == 6
