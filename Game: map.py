import random

def gen_mortes(hauteur_monde,largeur_monde,nbr_cases):
        cases_mortes=[]
        for i in range(nbr_cases):
            x=random.randint(0,largeur_monde)
            y=random.randint(0,hauteur_monde)
            i = [x,y]
            cases_mortes.append(i) 
        return cases_mortes


def extract(liste):
    listex=[]
    listey=[] 
    for item in liste:
        for i in item:
            if i==0:
                listex += i
            else:
                listey += i
             
    return listex, listey

#Je n'ai pas réussi à implémenter la fonction cases mortes en les générant aléatoirement. La seconde fonction sert à extraire les premiers termes de chaque liste et les mettre dans une autre liste x, même chose pour y, ainsi cela permettrait de générer aléatoirement des cases bloquées ou avec des monstres/objectifs et de faire un test pour savoir si le joueur se trouve à ces coordonnées x,y. Or je n'arrive pas à itérer sur les éléments de i

def use_map():
    pos_x=0
    pos_y=0
    hauteur_monde = int(input("Combien de cases de haut ?"))
    largeur_monde = int(input("Combien de cases de large ?"))
    cases_bloquées = int(input("Combien de cases mortes ?"))

    gen_mortes(hauteur_monde,largeur_monde,cases_bloquées)

    for y in range(hauteur_monde):
        for x in range(largeur_monde):
            if x == pos_x and y == pos_y:
                print("X", end =" ")
            else:
                print("_", end =" ")
        print()

    while True:

        cmd = str(input("Où voulez-vous aller ? 'haut', 'bas', 'gauche', 'droite'"))

        if cmd == "haut":
            pos_y -= 1
            if pos_y < 0 or pos_y > hauteur_monde-1:
                print("Vous êtes au bord de la carte")
                pos_y += 1
                pass
            else:
                for y in range(hauteur_monde):
                    for x in range(largeur_monde):
                        if x == pos_x and y == pos_y:
                            print("X", end=" ")
                        else:
                            print("_", end=" ")
                    print()            
        if cmd == "bas":
            pos_y += 1
            if pos_y < 0 or pos_y > hauteur_monde-1:
                print("Vous êtes au bord de la carte")
                pos_y -= 1
                pass
            else:
                for y in range(hauteur_monde):
                    for x in range(largeur_monde):
                        if x == pos_x and y == pos_y:
                            print("X", end=" ")
                        else:
                            print("_", end=" ")
                    print()            
        if cmd == "gauche":
            pos_x -= 1
            if pos_x < 0 or pos_x > largeur_monde-1:
                print("Vous êtes au bord de la carte")
                pos_x += 1
                pass
            else:
                for y in range(hauteur_monde):
                    for x in range(largeur_monde):
                        if x == pos_x and y == pos_y:
                            print("X", end=" ")
                        else:
                            print("_", end=" ")    
                print()
                                
        if cmd == "droite":
            pos_x += 1
            if pos_x < 0 or pos_x > largeur_monde-1:
                print("Vous êtes au bord de la carte")
                pos_x -= 1
                pass
            else:
                for y in range(hauteur_monde):
                    for x in range(largeur_monde):
                        if x == pos_x and y == pos_y:
                            print("X", end=" ")
                        else:
                            print("_", end=" ")  
                    print()              
 
