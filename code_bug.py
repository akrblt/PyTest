# code_bug.py

def ajouter(a, b):
    # Bug ici : ne retourne pas la somme correctement (exemple volontaire)
    return a + b

def est_adulte(age):
    # Bug ici : condition incorrecte (devrait être >= 18)
    if age >= 18:
        return True
    else:
        return False

def division(a, b):
    # Fonction correcte mais peut lever ZeroDivisionError
    return a / b

def multiplier(a,b):
    return a*b