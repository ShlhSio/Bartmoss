t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
t3 = []

def patchin2(liste1, liste2):
    n = 0
    liste3=[]
    while n < len(liste1):
        liste3.append(liste2[n])
        liste3.append(liste1[n])
        n+=1
    return liste3


def maxlist(liste):
    maximum = max(liste)
    return maximum
   
   
print(patchin2(t1,t2))
print(maxlist(t1))
