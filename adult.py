

def is_adult(age):
    if not isinstance(age,int):
        raise ValueError(" L`age doit etre un entier ")
    if age>=18:
        return True
    else:
        return False