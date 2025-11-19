import pytest

from unittest.mock import Mock

from inscriptionUtilisateurs import inscriptionUtilisateur
def test_inscription_valide():
    # Arrange
    email = "utilisateur@example.com"
    motDePasse = "motdepasse123"
    db = Mock()
    db.email_existe.return_value = False

    # Act
    utilisateur = inscriptionUtilisateur(email, motDePasse, db)

    # Assert
    assert utilisateur.email == email

def test_email_invalide():
    # Arrange
    email = "utilisateur.com"  # Sans '@'
    motDePasse = "motdepasse123"
    db = Mock()
    db.email_existe.return_value = False

    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        inscriptionUtilisateur(email, motDePasse, db)
    assert "Email invalide" in str(excinfo.value)

def test_motdepasse_trop_court():
    # Arrange
    email = "utilisateur@example.com"
    motDePasse = "123"  # Trop court
    db = Mock()
    db.email_existe.return_value = False

    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        inscriptionUtilisateur(email, motDePasse, db)
    assert "Mot de passe trop court" in str(excinfo.value)

def test_email_deja_utilise():
    # Arrange
    email = "utilisateur@example.com"
    motDePasse = "motdepasse123"
    db = Mock()
    db.email_existe.return_value = True  # Simule email déjà existant

    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        inscriptionUtilisateur(email, motDePasse, db)
    assert "Email déjà utilisé" in str(excinfo.value)

def test_format_incorrect_type():
    # Arrange
    email = None  # Mauvais type
    motDePasse = "motdepasse123"
    db = Mock()
    db.email_existe.return_value = False

    # Act & Assert
    with pytest.raises(TypeError) as excinfo:
        inscriptionUtilisateur(email, motDePasse, db)
    assert "email doit être une chaîne" in str(excinfo.value).lower()
