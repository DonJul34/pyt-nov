# statistiques.py

def calculer_chiffre_affaire_total(clients):
    """Calcule le chiffre d'affaires total généré par tous les clients."""
    total = sum(client.calculer_chiffre_affaire() for client in clients)
    return total

def clients_par_categorie(clients):
    """Compte le nombre de clients dans chaque catégorie."""
    categories = {}
    for client in clients:
        if client.categorie in categories:
            categories[client.categorie] += 1
        else:
            categories[client.categorie] = 1
    return categories

def afficher_statistiques(clients):
    """Affiche des statistiques générales sur les clients."""
    print("\n--- Statistiques CRM ---")
    print(f"Nombre total de clients : {len(clients)}")
    
    chiffre_affaire = calculer_chiffre_affaire_total(clients)
    print(f"Chiffre d'affaires total : {chiffre_affaire:.2f} €")
    
    categories = clients_par_categorie(clients)
    print("Nombre de clients par catégorie :")
    for categorie, count in categories.items():
        print(f"{categorie} : {count} clients")
