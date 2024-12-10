

numbers = [8, 7, 11, 2, 10, 5, 8]

# Méthode 1 : Utilisation d'un ensemble
result_set = list(set(numbers))
print("En utilisant un ensemble :", result_set)

# Méthode 2 : Utilisation d'une liste en compréhension avec un ensemble
seen = set()
result_comprehension = [x for x in numbers if x not in seen and not seen.add(x)]
print("En utilisant une liste en compréhension :", result_comprehension)

# Méthode 3 : Utilisation d'un dictionnaire
result_dict = list(dict.fromkeys(numbers))
print("En utilisant un dictionnaire :", result_dict)

# Méthode 4 : Utilisation d'une boucle for et d'une liste
result_loop = []
for num in numbers:
    if num not in result_loop:
        result_loop.append(num)
print("En utilisant une boucle for :", result_loop)