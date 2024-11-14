# main.py

from client import Client
from statistiques import afficher_statistiques
from admin import creer_client, modifier_client, supprimer_client

def menu():
    print("\n--- Menu CRM ---")
    print("1. Ajouter un client")
    print("2. Afficher les clients")
    print("3. Modifier un client")
    print("4. Supprimer un client")
    print("5. Afficher les statistiques")
    print("6. Quitter")

# Point d'entrée
if __name__ == "__main__":
    clients = []  # Liste pour stocker les clients
    
    while True:
        menu()
        choix = input("Sélectionnez une option : ")

        if choix == "1":
            client = creer_client()
            clients.append(client)
            print(f"Client {client.nom} ajouté avec succès.")
        
        elif choix == "2":
            for client in clients:
                print(client.afficher_infos())

        elif choix == "3":
            nom_client = input("Entrez le nom du client à modifier : ")
            client_a_modifier = next((c for c in clients if c.nom == nom_client), None)
            if client_a_modifier:
                modifier_client(client_a_modifier)
                print(f"Client {client_a_modifier.nom} modifié.")
            else:
                print(f"Client {nom_client} non trouvé.")

        elif choix == "4":
            nom_client = input("Entrez le nom du client à supprimer : ")
            clients = supprimer_client(clients, nom_client)

        elif choix == "5":
            afficher_statistiques(clients)
        elif choix == "7":
            clients_par_categorie(clients)
        elif choix == "6":
            print("Au revoir !")
            break

        else:
            print("Option non valide, veuillez réessayer.")
