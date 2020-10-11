def carre(x):
    return x*x


def TriangleRectangle(a,b,c):
    if carre(a) == carre(b)+carre(c):
        return True
    else:
        return False

continuer = True
while continuer:
    a = int(input("longueur du premier côté >"))
    b = int(input("longueur du deuxième côté >"))
    c = int(input("longueur du troisième côté >"))

    [a, b, c] = sorted([a, b, c], reverse=True)
    print(TriangleRectangle(a, b, c))
    
    ordre = input("Si vous voulez-vous continuer tapez oui >")
    if ordre == "oui":
        continuer = True
    else:
        continuer = False
