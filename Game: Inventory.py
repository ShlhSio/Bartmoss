import random

def use_inventory():
    objets = ["brique","orange","pièce","épée","lanterne","luth","lama","heaume","jacques"]
    inventaire = []
    au_sol = random.choices(objets, k=4)
    au_sol.sort()

    while True:
        print(f"--> Au sol : {au_sol} et dans votre   inventaire : {inventaire}")
        cmd = str(input("Que faites vous ? 'prendre', 'poser', 'créer', 'détruire' +'objet' ou 'quitter' :")).lower().split()
        
        
        if cmd[0]=="prendre":
            print(f"Vous décidez de {cmd[0]} '{cmd[1]}''")
            print(prendre(inventaire,au_sol,cmd[1]))
        elif cmd[0]=="poser":
            print(f"Vous décidez de {cmd[0]} '{cmd[1]}''")
            print(poser(inventaire,au_sol,cmd[1]))
        elif cmd[0]=="créer":
            print(creer(inventaire,cmd[1]))
        elif cmd[0]=="détruire":
            print(detruire(inventaire,cmd[1]))
        elif cmd[0]=="quitter":
            break
        else:
            print("Veuillez entrer une action valide")


def prendre(liste1,liste2,x):
    if x in liste2 :
        liste2.remove(x)
        liste1.append(x)
    else:
        print(f"{x} n'est pas au sol")
    return 


def poser(liste1,liste2,x):
    if x in liste1:
        liste1.remove(x)
        liste2.append(x)
    else:
        print(f"{x} n'est pas dans votre inventaire")
    return 


def detruire(liste1, x):
    if x in liste1:
        liste1.remove(x)
    else:
        print(f"{x} n'est pas là")
    return 


def creer(liste1, x):
    liste1.append(x)
    print(f"Grâce à vos pouvoirs magiques vous créez {x}")
    return 
