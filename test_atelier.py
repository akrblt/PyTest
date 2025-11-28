"""
Burayi unittest ile yaptim bunun syntax i pytest ten biraz farki
import unittest
from atelier import calculerPrixAvecemise
class TestCalculerPrixAvecRemise(unittest.TestCase):
    def test_remise_base(self):
        self.assertEqual(calculerPrixAvecemise(200,10),180)


    def test_remise_zero(self):
        self.assertEqual(calculerPrixAvecemise(200,0),200)

    def test_totalHT_zero(self):
        self.assertEqual(calculerPrixAvecemise(0,10),0)

    def test_remise_negatif(self):
        with self.assertRaises(ValueError):
            calculerPrixAvecemise(200,-5)

    def test_remise_superieure_100(self):
        with self.assertRaises(ValueError):
            calculerPrixAvecemise(200,150)

    def test_types_incorrects(self):
        with self.assertRaises(TypeError):
            calculerPrixAvecemise("200",0.5)
        with self.assertRaises(TypeError):
            calculerPrixAvecemise(200,"25")

if __name__ == '__main__':
    unittest.main()
"""
import  pytest
from atelier import calculerPrixAvecemise

def test_remise_base():
    assert calculerPrixAvecemise(200,10)==180

def test_remise_zero():
    assert calculerPrixAvecemise(200,0)==200

def test_totalHT_zero():
    assert calculerPrixAvecemise(0,5)==0

def test_remise_negatif():
    with pytest.raises(ValueError) as e:
     calculerPrixAvecemise(200,-5)
     assert str(e.value) =="remise dois etre entre 0 et 100"

def test_remise_superieure_100():
    with pytest.raises(ValueError):
        calculerPrixAvecemise(250,120)

def test_type_remise_incorrect():
    with pytest.raises(TypeError):
        calculerPrixAvecemise(120,"25")

def test_type_totalHT_incorrect():
    with pytest.raises(TypeError):
        calculerPrixAvecemise("250",25)