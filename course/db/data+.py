import json
import re

# Charger le fichier JSON
with open('c:/Users/Lenovo/Desktop/ipi_python/course/db/users.json', 'r') as f:
    data:dict = json.load(f)

# 1. Supprimer le second utilisateur
del data['users'][1]

# 2. Ajouter un ami au troisième utilisateur
data['users'][2]['friends'].append({'id': 3, 'name': 'NouveauAmi'})

# 3. Mettre à jour le numéro de téléphone du quatrième utilisateur
data['users'][3]['phone'] = '+1(954) 421-6824'

# 4. Ajouter une deuxième entreprise au premier utilisateur
data['users'][0]['company'] += ', SYLENT'

# 5. Séparer nom et prénom
for utilisateur in data['users']:
    nom_complet = utilisateur['name'].split()
    utilisateur['firstName'] = nom_complet[0]
    utilisateur['lastName'] = nom_complet[1]
    del utilisateur['name']

# 6. Supprimer le tag "laborum" du dernier utilisateur
data['users'][-1]['tags'].remove('laborum')

# 7. Ajouter +1 à l'âge de tous les utilisateurs
for utilisateur in data['users']:
    utilisateur['age'] += 1

# Écrire le fichier JSON modifié
with open('c:/Users/Lenovo/Desktop/ipi_python/course/db/users_modifie.json', 'w') as f:
    json.dump(data, f, indent=4)