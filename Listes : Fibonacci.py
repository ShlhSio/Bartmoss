def listfibo():
    termes = int(input("Combien de termes ?"))
    a, b = 0, 1
    compteur = 0
    liste = []
    while compteur < termes:
        liste.append(a)
        c = a + b
        a = b
        b = c
        compteur += 1
    return liste

print(listfibo())
