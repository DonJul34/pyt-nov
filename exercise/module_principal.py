# module_principal.py
import logging

# Configuration du logger
file_handler = logging.FileHandler('erreurs.log', encoding='utf-8')
file_handler.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.ERROR)
logger.addHandler(file_handler)

def master():
    logger.error("Exécution directe : Ce message apparaît seulement si le script est exécuté directement.")
    print("Le script est exécuté directement.")


if __name__ == "__main__": #est vrai seulement si on éxecute module_principal.py
    master() 
else: #Si module_principal.py est executé dans un autre module python (module_import.py)
    logger.error("Importation : Ce message apparaît lors de l'import dans un autre module.")
    print("Le script est importé dans un autre module.")
