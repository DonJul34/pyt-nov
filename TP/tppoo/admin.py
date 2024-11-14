# admin.py

from client import Client

def creer_client():
    """Crée un nouveau client."""
    nom = input("Nom du client : ")
    email = input("Email du client : ")
    telephone = input("Téléphone du client : ")
    
    categorie = input("Catégorie (SEO/Web/Autre) : ").capitalize()
    prix_par_employe = 7 if categorie in ["SEO", "Web"] else 5
    
    while True:
        try:
            nombre_employes = int(input("Nombre d'employés : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    return Client(nom, email, telephone, categorie, nombre_employes, prix_par_employe)

def modifier_client(client):
    """Permet de modifier les informations d'un client existant."""
    client.nom = input(f"Nouveau nom (actuel: {client.nom}) : ") or client.nom
    client.email = input(f"Nouvel email (actuel: {client.email}) : ") or client.email
    client.telephone = input(f"Nouveau téléphone (actuel: {client.telephone}) : ") or client.telephone
    client.categorie = input(f"Nouvelle catégorie (actuelle: {client.categorie}) : ").capitalize() or client.categorie
    return client

def supprimer_client(clients, nom_client):
    """Supprime un client de la liste."""
    clients = [client for client in clients if client.nom != nom_client]
    print(f"Le client {nom_client} a été supprimé.")
    return clients
