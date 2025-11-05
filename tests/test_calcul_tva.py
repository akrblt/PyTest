import pytest

from calcul_tva import calculer_prix_ttc

def test_standart():
     ht=100
     tva=0.2
     resultat_attendu=120.0
     assert calculer_prix_ttc(ht,tva)==resultat_attendu

def test_erreur_prix_negatif():
    ht=-50
    tva=0.2
    with pytest.raises(ValueError):

        calculer_prix_ttc(ht,tva)

def test_erreur_prix_negatif_with_message():
    ht=-50
    tva=0.2
    with pytest.raises(ValueError) as e:
        calculer_prix_ttc(ht,tva)
        assert str(e.value)=="prix_ht et tva doivent être positifs"

def test_erreur_tva_negatif():
    ht=50
    tva=-0.2
    with pytest.raises(ValueError):
        calculer_prix_ttc(ht,tva)

def test_limite_prix_zero():
    ht=0
    tva=0.2
    calculer_prix_ttc(ht,tva)==0.0

def test_type_invalide():
    ht="cent"
    tva=0.2
    with pytest.raises(TypeError):
        calculer_prix_ttc(ht,tva)