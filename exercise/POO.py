from datetime import datetime, timedelta

# Exception personnalisée
class LivreIndisponibleError(Exception):
    pass

# Classe Livre
class Livre:
    def __init__(self, titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        return f"{self.titre} par {self.auteur} (ISBN: {self.isbn}) - {'Disponible' if self.disponible else 'Emprunté'}"

# Classe Utilisateur
class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.emprunts = []

    def emprunter(self, livre, bibliotheque):
        try:
            bibliotheque.emprunter_livre(self, livre)
            print(f"{self.nom} a emprunté {livre.titre}.")
        except LivreIndisponibleError as e:
            print(e)

    def retourner(self, livre, bibliotheque):
        bibliotheque.retourner_livre(self, livre)
        print(f"{self.nom} a retourné {livre.titre}.")

    def __str__(self):
        return f"Utilisateur: {self.nom}"

# Classe Employe qui hérite de Utilisateur
class Employe(Utilisateur):
    def __init__(self, nom, identifiant):
        super().__init__(nom)
        self.identifiant = identifiant

    def ajouter_livre(self, livre, bibliotheque):
        bibliotheque.ajouter_livre(livre)
        print(f"Livre ajouté par {self.nom} : {livre}")

    def supprimer_livre(self, livre, bibliotheque):
        bibliotheque.supprimer_livre(livre)
        print(f"Livre supprimé par {self.nom} : {livre}")

    def __str__(self):
        return f"Employé: {self.nom} (ID: {self.identifiant})"

# Classe Bibliotheque
class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = []
        self.historique_emprunts = {}

    def ajouter_livre(self, livre):
        self.catalogue.append(livre)
        print(f"Livre ajouté au catalogue : {livre}")

    def supprimer_livre(self, livre):
        if livre in self.catalogue:
            self.catalogue.remove(livre)
            print(f"Livre retiré du catalogue : {livre}")
        else:
            print("Livre introuvable dans le catalogue.")

    def emprunter_livre(self, utilisateur, livre):
        if livre in self.catalogue and livre.disponible:
            livre.disponible = False
            utilisateur.emprunts.append((livre, datetime.now()))
            self.historique_emprunts[utilisateur.nom] = self.historique_emprunts.get(utilisateur.nom, []) + [(livre, "emprunté")]
        else:
            raise LivreIndisponibleError(f"Le livre '{livre.titre}' n'est pas disponible pour l'emprunt.")

    def retourner_livre(self, utilisateur, livre):
        if livre in [emprunt[0] for emprunt in utilisateur.emprunts]:
            livre.disponible = True
            utilisateur.emprunts = [(l, d) for l, d in utilisateur.emprunts if l != livre]
            self.historique_emprunts[utilisateur.nom].append((livre, "retourné"))
        else:
            print("Ce livre n'a pas été emprunté par cet utilisateur.")

    def afficher_catalogue(self):
        print(f"\nCatalogue de la bibliothèque {self.nom} :")
        for livre in self.catalogue:
            print(livre)

    def afficher_historique_emprunts(self, utilisateur):
        print(f"\nHistorique des emprunts pour {utilisateur.nom} :")
        for livre, action in self.historique_emprunts.get(utilisateur.nom, []):
            print(f"{livre.titre} - {action}")

# Utilisation du code

# Création de la bibliothèque
bibliotheque = Bibliotheque("Bibliothèque Centrale")

# Création des livres
livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "123456789")
livre2 = Livre("Les Misérables", "Victor Hugo", "987654321")

# Création des utilisateurs
utilisateur1 = Utilisateur("Alice")
utilisateur2 = Utilisateur("Bob")
employe1 = Employe("Claire", identifiant=101)

# Ajout des livres par un employé
employe1.ajouter_livre(livre1, bibliotheque)
employe1.ajouter_livre(livre2, bibliotheque)

# Affichage du catalogue
bibliotheque.afficher_catalogue()

# Emprunt et retour de livres
utilisateur1.emprunter(livre1, bibliotheque)
utilisateur2.emprunter(livre1, bibliotheque)  # Devrait afficher une erreur de disponibilité
utilisateur1.retourner(livre1, bibliotheque)
utilisateur2.emprunter(livre1, bibliotheque)  # Devrait fonctionner maintenant

# Historique des emprunts
bibliotheque.afficher_historique_emprunts(utilisateur1)
bibliotheque.afficher_historique_emprunts(utilisateur2)
