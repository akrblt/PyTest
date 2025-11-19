import unittest
from inverser import inverserTexte


class TestInverserTexte(unittest.TestCase):

    def test_inverserTexte(self):
        # Test principal : inverser une chaîne simple
        self.assertEqual(inverserTexte("chat"), "tahc")

    def test_chaine_vide(self):
        # Test pour une chaîne vide
        self.assertEqual(inverserTexte(""), "")

    def test_chaine_un_caractere(self):
        # Test pour une chaîne d'un seul caractère
        self.assertEqual(inverserTexte("a"), "a")

    def test_chaine_avec_espaces(self):
        # Test pour une chaîne avec des espaces
        self.assertEqual(inverserTexte("hello world"), "dlrow olleh")


if __name__ == '__main__':
    unittest.main()