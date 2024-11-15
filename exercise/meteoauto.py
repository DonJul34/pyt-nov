import sqlite3
from datetime import datetime
from meteofrance_api import MeteoFranceClient

# Initialiser le client Météo-France
client = MeteoFranceClient()

# Liste des villes à surveiller
villes = ["Paris", "Lyon", "Marseille"]

# Connexion à la base de données SQLite
conn = sqlite3.connect('meteo.db')
cursor = conn.cursor()

# Création de la table si elle n'existe pas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS meteo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ville TEXT,
        date TEXT,
        temperature_min REAL,
        temperature_max REAL,
        description TEXT,
        date_enregistrement TEXT
    )
''')

# Fonction pour insérer les données dans la base
def inserer_donnees(ville, date, temp_min, temp_max, description):
    cursor.execute('''
        INSERT INTO meteo (ville, date, temperature_min, temperature_max, description, date_enregistrement)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (ville, date, temp_min, temp_max, description, datetime.now().isoformat()))
    conn.commit()

# Récupérer et insérer les données pour chaque ville
for ville in villes:
    # Recherche de la ville
    lieux = client.search_places(ville)
    if lieux:
        lieu = lieux[0]  # Prendre le premier résultat
        # Récupérer les prévisions
        previsions = client.get_forecast_for_place(lieu)
        # Obtenir les prévisions du jour
        prevision_aujourdhui = previsions.daily_forecast[0]
        print(prevision_aujourdhui)
        # Insérer les données dans la base
        # Insérer les données dans MongoDB
        inserer_donnees(
            ville=lieu.name,
            date=prevision_aujourdhui.get("datetime", "Date inconnue"),  # Adaptez la clé si nécessaire
            temp_min=prevision_aujourdhui.get("T_min", None),
            temp_max=prevision_aujourdhui.get("T_max", None),
            description=prevision_aujourdhui.get("weather12H", {}).get("desc", "Description indisponible")
        )

        print(f"Données pour {ville} insérées avec succès.")
    else:
        print(f"Ville {ville} non trouvée.")

# Fermeture de la connexion à la base de données
conn.close()
