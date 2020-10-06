secondes = int(input("Nombre de secondes ? >"))

minute = 60
heure = minute * 60
jour = heure * 24
mois = jour * 30
année = mois * 12

années = secondes // année
secondes = secondes % année

nbmois = secondes // mois
secondes = secondes % mois

jours = secondes // jour
secondes = secondes % jour

heures = secondes // heure
secondes = secondes % heure

minutes = secondes // minute
secondes = secondes % minute


print(f"{années} années, {nbmois} mois, {jours} jours, {heures} heures, {minutes} minutes, {secondes} secondes")
