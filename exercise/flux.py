import logging

file_handler = logging.FileHandler('erreurs.log', encoding='utf-8')
file_handler.setLevel(logging.ERROR)

# Définir le format des messages de log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Configurer le logger de base
logging.getLogger().addHandler(file_handler)
logging.getLogger().setLevel(logging.ERROR)

# Exemple d'utilisation
logging.error("Erreur de test avec des accents : éèàç")

chiffre1 = int(input("Entrez le numéro : "))

if chiffre1 < 0:
    print(f"le chiffre {chiffre1} est négatif")
elif chiffre1 == 0:
    print(f"le chiffre {chiffre1} est zéro")
else:
    print(f"le chiffre {chiffre1} est positif")

#Nombre paire entre 1 et 20.

for i in range(1,21):
    if i % 2  == 0:
        print(i)
        
#password        
correct_pass = "PYT"
password = ""
while password != correct_pass:
    password = input("Saisissez le mot de passe :")
    if password != correct_pass:
        print("Mot de passe incorect, essayer de nouveau")
    else:
        print("Mot de passe correct, accès autorisé.")
        
        
        
#exception

try:   
    nombre_division = float(input("Saississez un nombre pour diviser 100"))
    result = 100 / nombre_division
    print(f"100 divisé par {nombre_division} est égal à {result}")
except ZeroDivisionError as e:
    logging.error("Erreur : Division par zéro impossible", exc_info=True)
    print(f"Erreur : Division par zéro impossible. Erreur : {e}")
except ValueError as e:
    logging.error("Erreur : Entrée invalide, un nombre est requis", exc_info=True)
    print("Erreur : Entrée invalide. Veuillez saisir un nombre.")
except Exception as e:
    logging.error("Une erreur inattendue s'est produite", exc_info=True)
    print(f"Erreur : Division par zéro impossible. Erreur : {e}")
