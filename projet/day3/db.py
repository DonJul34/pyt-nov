import sqlite3
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log")
    ]
)

def creer_table_clients():
    connection = sqlite3.connect('clients.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            email TEXT,
            telephone TEXT,
            categorie TEXT,
            nombre_employes INTEGER,
            prix_par_employe REAL,
            cout_ht REAL,
            cout_ttc REAL
        )
    ''')
    connection.commit()
    connection.close()
    return "Success"
    
def ajouter_client_bd(client):
    connection = sqlite3.connect('clients.db')
    cursor = connection.cursor()
       
    cursor.execute('''
        INSERT INTO clients (nom, email, telephone, categorie, nombre_employes, prix_par_employe, cout_ht, cout_ttc)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (client.nom, client.email, client.telephone, client.categorie, client.nombre_employes, client.prix_par_employe, client.cout_ht, client.cout_ttc))
    connection.commit()
    connection.close()


def recuperer_clients_bd():
    """Récupère tous les clients depuis la base de données."""
    connection = sqlite3.connect('clients.db')
    cursor = connection.cursor()

    try:
        cursor.execute('SELECT * FROM clients')
        column_names = [description[0] for description in cursor.description]

    except Exception as e:
        print("Impossible de selectionner les Clients" + str(e))
        logging.error("Erreur : un problème sérieux est survenu lors de la récupération des clients" + str(e))
  

    clients = cursor.fetchall()
    clients_dict = [dict(zip(column_names, client)) for client in clients]
    print(clients_dict)
    connection.close()
    return clients
