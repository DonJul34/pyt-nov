from pymongo import MongoClient

# Connexion à la base MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['chatgpt']
collection = db['chat_history']

# Fonction pour enregistrer un message
def save_message(role, content):
    collection.insert_one({'role': role, 'content': content, 'timestamp': datetime.datetime.now()})

# Fonction pour récupérer l'historique des messages
def get_chat_history():
    return list(collection.find({}, {'_id': 0, 'role': 1, 'content': 1}).sort('timestamp', 1))
