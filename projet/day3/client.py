class Client:
    """Classe représentant un client dans le CRM."""
    
    def __init__(self, nom, email, telephone, categorie, nombre_employes, prix_par_employe):
        """Constructeur de la classe Client."""
        self.nom = nom
        self.email = email
        self.telephone = telephone
        self.categorie = categorie
        self.nombre_employes = nombre_employes
        self.prix_par_employe = prix_par_employe
        self.cout_ht = 20 + prix_par_employe * nombre_employes  # Coût HT (fixe + prix par employé)
        self.cout_ttc = self.cout_ht * 1.20  # Coût TTC avec TVA 20%
    
    def __str__(self):
        return (f"Nom: {self.nom}, Email: {self.email}, Téléphone: {self.telephone}, "
                f"Catégorie: {self.categorie}, Nombre d'employés: {self.nombre_employes}, "
                f"Coût HT: {self.cout_ht:.2f} €, Coût TTC: {self.cout_ttc:.2f} €")

    def afficher_infos(self):
        """Méthode pour afficher les informations du client."""
        return (f"Nom: {self.nom}, Email: {self.email}, Téléphone: {self.telephone}, "
                f"Catégorie: {self.categorie}, Nombre d'employés: {self.nombre_employes}, "
                f"Coût HT: {self.cout_ht:.2f} €, Coût TTC: {self.cout_ttc:.2f} €")

    def calculer_chiffre_affaire(self):
        """Méthode pour renvoyer le chiffre d'affaires généré par ce client."""
        return self.cout_ttc
