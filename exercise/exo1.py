#Pour filtrer hors les accent 
import locale

# Configurer la locale en français pour le tri
locale.setlocale(locale.LC_COLLATE, 'fr_FR.UTF-8')

# Liste à trier
liste = ["école", "éléphant", "avion", "âge", "zèbre", "être"]

# Trier la liste en utilisant les règles de tri de la locale
liste_triee = sorted(liste, key=locale.strxfrm)

print(liste_triee)


# Étape 1 : Créer une liste de nombres
numbers = [1, 2, 3, 4, 5]

# Étape 2 : Ajouter un nouvel élément à la liste
numbers.append(6)
numbers.insert(3, 6)  # Ajoute 6 à l'index 3 (4e position)
numbers = numbers + [6]

# Étape 3 : Convertir la liste en un tuple
numbers_tuple = tuple(numbers)

# Étape 4 : Créer un dictionnaire contenant des informations sur une personne
person_info = {
    "nom": "Alice",
    "âge": 30,
    "profession": "Développeur"
}

# Étape 5 : Ajouter un set pour les compétences de cette personne
skills_set = {"Python", "JavaScript", "SQL"}
person_info["compétences"] = skills_set

# Étape 6 : Imprimer toutes les informations de manière structurée
print("Liste des nombres :", numbers)
print("Tuple des nombres :", numbers_tuple)
print("\nInformations sur la personne :")
print(f"Nom : {person_info['nom']}")
print(f"Âge : {person_info['âge']}")
print(f"Profession : {person_info['profession']}")
print(f"Compétences : {', '.join(person_info['compétences'])}")