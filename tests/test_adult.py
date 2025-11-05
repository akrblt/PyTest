import pytest

from adult import is_adult

def test_exactly_18():
    assert is_adult(18)==True

def test_mineur_18():
    assert is_adult(17)==False

def test_majeur_18():
    assert is_adult(45)==True

def test_age_zero():
    assert is_adult(0)==False

def test_age_negatif():
    assert is_adult(-5)==False

def test_type_incorrect():
#   assert is_adult("dix-huit")==ValueError
# bu satir calismaz cunku assert ile ValueError u karsilastiramayiz
    with pytest.raises(ValueError) :
        is_adult("dix-huit")

# eger hata mesajinida kontrol etmek istiyorsak
def test_type_incorrect_with_message():
    with pytest.raises(ValueError) as e:
        is_adult("dix-huit")
        assert str(e.value) == " L`age doit etre un entier "