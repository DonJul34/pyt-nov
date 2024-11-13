#Etape 1 Créer un programme qui demande à l'utilisateur de saisir deux nombres.

chiffre1 = int(input("Entrez le numéro : "))
chiffre2 = int(input("Entrez le numéro numéro 2: "))

#Etape 2: Effectuer les opérations arithmétiques de base (+, -, *, /) sur ces deux nombres et afficher les résultats.
addition = chiffre1 + chiffre2
soustraction = chiffre1 - chiffre2
division = chiffre1 / chiffre2 if chiffre2 != 0 else "Division par zéro impossible" 
multiplication = chiffre1 * chiffre2 if chiffre2 != 0 else "Multplication par zéro impossible" 

print(f"Addition des deux chiffres {str(addition)}")
print("Soustraction des deux chiffres " + str(soustraction))
print("Division " + str(division))
print("Multiplication des deux chiffres " + str(multiplication))

#Etape 3 Demander à l'utilisateur de saisir une chaîne, puis l'afficher en utilisant un f-string.

Nom = input("Entrez votre nom : ")
Prenom = input("Entrez votre Prénom : ")
Age = int(input("Entrez votra age:"))
print(f"Bonjour,{Prenom} {Nom} ! Vous avez {str(Age)} ans")

#Etape 4 Utiliser les opérateurs logiques pour vérifier si le premier nombre est supérieur ou égal au second.
results = chiffre1 >= chiffre2
text_to_show = "Company"
print("Company" + str(results)) #Est-ce que le nombre est

if chiffre1 <= chiffre2:
    print(f"Le chiffre {str(chiffre1)} est plus petit ou égal que {str(chiffre2)}, logiciel par {text_to_show}")
else:
    print(f"Le chiffre {str(chiffre1)} est plus grand que {str(chiffre2)}")
