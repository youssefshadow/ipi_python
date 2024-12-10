import json
import re

with open('c:/Users/Lenovo/Desktop/ipi_python/course/db/users.json', 'r') as f:
    data = json.load(f)

# 1. Nombre d'utilisateurs
nombre_utilisateurs = len(data['users'])
print(" Q1: Nombre d'utilisateurs :", nombre_utilisateurs)

# 2. Entreprise du second utilisateur
entreprise_deuxieme_utilisateur = data['users'][1]['company']
print("Q2: L'entreprise du deuxième utilisateur est :", entreprise_deuxieme_utilisateur)

# 3. Nom complet du troisième ami du second utilisateur
nom_troisieme_ami_deuxieme_utilisateur = data['users'][1]['friends'][2]['name']
print("Q3: Le nom complet du troisième ami du deuxième utilisateur est :", nom_troisieme_ami_deuxieme_utilisateur)

# 4. Couleur des yeux du premier utilisateur
couleur_yeux_premier_utilisateur = data['users'][0]['eyeColor']
print("Q4 :La couleur des yeux du premier utilisateur est :", couleur_yeux_premier_utilisateur)

# 5. Adresse de chacun des utilisateurs
print("Adresses des utilisateurs :")
for utilisateur in data['users']:
    print(utilisateur['address'])

# 6. Nombre d'utilisateurs dont le fruit favoris est la fraise
nombre_amateurs_fraise = sum(1 for utilisateur in data['users'] if utilisateur['favoriteFruit'] == 'strawberry')
print("Q6: Nombre d'utilisateurs préférant la fraise :", nombre_amateurs_fraise)

# 7. Nombre de messages non lus de Brianna Huffman
for utilisateur in data['users']:
    if utilisateur['name'] == 'Brianna Huffman':
        # Utiliser une expression régulière pour extraire le nombre
        match = re.search(r'(\d+) unread messages', utilisateur['greeting'])
        if match:
            messages_non_lus_brianna = int(match.group(1))
            print("Q7: Brianna Huffman a", messages_non_lus_brianna, "messages non lus.")
        else:
            print("Impossible d'extraire le nombre de messages pour Brianna Huffman.")
        break

# 8. Pourcentage d'utilisateurs masculins
nombre_hommes = sum(1 for utilisateur in data['users'] if utilisateur['gender'] == 'male')
pourcentage_hommes = (nombre_hommes / nombre_utilisateurs) * 100
print("Q8: Pourcentage d'utilisateurs masculins :", pourcentage_hommes, "%")

# 9. Moyenne d'âge des utilisateurs féminines
ages_femmes = [float(utilisateur['balance'][1:].replace(',', '')) for utilisateur in data['users'] if utilisateur['gender'] == 'female']
moyenne_age_femmes = sum(ages_femmes) / len(ages_femmes)
print("Q9: Moyenne d'âge des femmes :", moyenne_age_femmes)

# 10. Somme des soldes de tous les utilisateurs
soldes = [float(utilisateur['balance'][1:].replace(',', '')) for utilisateur in data['users']]
somme_soldes = sum(soldes)
print("Q10: Somme des soldes :", somme_soldes)

# 11. Ville où réside Zelma Sutton
for utilisateur in data['users']:
    if utilisateur['name'] == 'Zelma Sutton':
        ville_zelma = utilisateur['address'].split(',')[1].strip()
        print("Q11:Zelma Sutton réside à :", ville_zelma)
        
        
        
        
        
      