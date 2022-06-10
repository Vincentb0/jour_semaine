"""
Programme qui renvoi le jour de la semaine
Site de vérification : https://www.ephemeride.com/calendrier/jour_semaine/80/?day=1&month=5&year=2022
"""

print("Entrez une date :")

# VARIABLES
jour = int(input("jour : "))
mois = int(input("mois : "))
annee = int(input("année : "))
anne_bissextile = annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0
jour_semaine = ""

while (jour <= 0 or jour > 31) or (mois <= 0 or mois > 12) or ((anne_bissextile and jour > 29) or (not anne_bissextile and jour > 28)) or (jour > 30 and (mois == 4 or mois == 6 or mois == 9 or mois == 11)):
        print("date invalide, entrez une date correcte :")
        jour = int(input("jour : "))
        mois = int(input("mois : "))
        annee = int(input("année : "))

# CALCULS
resultat = annee % 100  # RECUPERE LES 2 DERNIERS CHIFFRES DU NOMBRE
resultat = resultat + (resultat // 4)  # // DIVISION ENTIERE
resultat = resultat + jour
date_invalide = False

# étude des cas
match mois:
    case 1 | 10:
        resultat += 1
    case 2 | 3 | 11:
        resultat += 4
    case 5:
        resultat += 2
    case 6:
        resultat += 5
    case 8:
        resultat += 3
    case 9 | 12:
        resultat += 6

if anne_bissextile and (mois == 1 or mois == 2):
    resultat -= 1

if annee >= 1600 and annee < 1700:
    resultat += 6
elif annee >= 1700 and annee < 1800:
    resultat += 4
elif annee >= 1800 and annee < 1900:
    resultat += 2
elif annee >= 2000 and annee < 2100:
    resultat += 6
elif annee == 2100:
    resultat += 4

resultat = resultat % 7

match resultat:
    case 1:
        jour_semaine = "Dimanche"
    case 2:
        jour_semaine = "Lundi"
    case 3:
        jour_semaine = "Mardi"
    case 4:
        jour_semaine = "Mercredi"
    case 5:
        jour_semaine = "Jeudi"
    case 6:
        jour_semaine = "Vendredi"
    case 0:
        jour_semaine = "Samedi"

print(f"Le {jour} / {mois} / {annee} correspond à un {jour_semaine}")