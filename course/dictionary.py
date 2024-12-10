chiffres_lettres = {
    '0': 'zéro',
    '1': 'un',
    '2': 'deux',
    '3': 'trois',
    '4': 'quatre',
    '5': 'cinq',
    '6': 'six',
    '7': 'sept',
    '8': 'huit',
    '9': 'neuf'
}

numero = input("Veuillez saisir un numéro de téléphone : ")
epellation = ""

for chiffre in numero:
    epellation += chiffres_lettres.get(chiffre, "inconnu") + " "

print(epellation.strip()) 