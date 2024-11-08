import random

nombre_aleatoire = random.randint(0, 100)
nombre_coups = 0

print("Bienvenue dans le jeu du nombre mystère !")
print("J'ai choisi un nombre entre 0 et 100. À vous de le trouver !")

while True:
    proposition = int(input("Quel est votre nombre ? "))
    nombre_coups += 1

    if proposition < nombre_aleatoire:
        print("C'est plus !")
    elif proposition > nombre_aleatoire:
        print("C'est moins !")
    else:
        print(f"Félicitations, vous avez trouvé le nombre en {nombre_coups} coups !")
        break