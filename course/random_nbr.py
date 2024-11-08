import random

def choisir_difficulte():
    while True:
        difficulte = input("Choisissez votre niveau de difficulté (facile, moyen, difficile) : ")
        if difficulte.lower() == "facile":
            return 10
        elif difficulte.lower() == "moyen":
            return 100
        elif difficulte.lower() == "difficile":
            return 1000
        else:
            print("Veuillez choisir une difficulté valide (facile, moyen ou difficile).")

# Fonction principale du jeu
def jouer():
    limite = choisir_difficulte()
    nombre_aleatoire = random.randint(0, limite)
    nombre_coups = 0

    print("Bienvenue dans le jeu du nombre mystère !")
    print(f"J'ai choisi un nombre entre 0 et {limite}. À vous de le trouver !")

    while True:
        try:
            proposition = int(input("Quel est votre nombre ? "))
        except ValueError:
            print("Veuillez entrer un nombre entier.")
            continue

        nombre_coups += 1

        if proposition < nombre_aleatoire:
            print("C'est plus !")
        elif proposition > nombre_aleatoire:
            print("C'est moins !")
        else:
            print(f"Félicitations, vous avez trouvé le nombre en {nombre_coups} coups !")
            break

# Appel de la fonction principale
jouer()
