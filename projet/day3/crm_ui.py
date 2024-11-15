import tkinter as tk
from tkinter import messagebox, ttk  # ttk pour le Treeview
from client import Client
from db import creer_table_clients, ajouter_client_bd, recuperer_clients_bd

class CRMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestionnaire CRM")
        
        self.form_frame = tk.Frame(root)
        self.form_frame.pack(side=tk.TOP, fill=tk.X, pady=20, padx=20)

        self.stat_frame = tk.Frame(root)
        self.stat_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=20, padx=20)

        self.tree_frame = tk.Frame(root)
        self.tree_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=20, padx=20)
        # Création des éléments graphiques
        self.label_nom = tk.Label(self.form_frame, text="Nom")
        self.label_nom.grid(row=0, column=0)
        self.entry_nom = tk.Entry(self.form_frame)
        self.entry_nom.grid(row=0, column=1)
        self.label_email = tk.Label(self.form_frame, text="Email")
        self.label_email.grid(row=1, column=0)
        self.entry_email = tk.Entry(self.form_frame)
        self.entry_email.grid(row=1, column=1)

        self.label_telephone = tk.Label(self.form_frame, text="Téléphone")
        self.label_telephone.grid(row=2, column=0)
        self.entry_telephone = tk.Entry(self.form_frame)
        self.entry_telephone.grid(row=2, column=1)

        self.label_categorie = tk.Label(self.form_frame, text="Catégorie (SEO/Web/Autre)")
        self.label_categorie.grid(row=3, column=0)
        self.entry_categorie = tk.Entry(self.form_frame)
        self.entry_categorie.grid(row=3, column=1)

        self.label_employes = tk.Label(self.form_frame, text="Nombre d'employés")
        self.label_employes.grid(row=4, column=0)
        self.entry_employes = tk.Entry(self.form_frame)
        self.entry_employes.grid(row=4, column=1)

        # Bouton pour ajouter un client
        self.btn_ajouter = tk.Button(self.form_frame, text="Ajouter Client", command=self.ajouter_client)
        self.btn_ajouter.grid(row=5, column=0, columnspan=2)

        # Configuration du Treeview pour afficher les clients
        self.tree = ttk.Treeview(self.tree_frame, columns=("nom", "email", "telephone", "categorie", "employes", "cout_ht", "cout_ttc"), show="headings")
        self.tree.heading("nom", text="Nom")
        self.tree.heading("email", text="Email")
        self.tree.heading("telephone", text="Téléphone")
        self.tree.heading("categorie", text="Catégorie")
        self.tree.heading("employes", text="Nombre d'employés")
        self.tree.heading("cout_ht", text="Coût HT (€)")
        self.tree.heading("cout_ttc", text="Coût TTC (€)")

        # Redimensionnement des colonnes
        self.tree.column("nom", width=100)
        self.tree.column("email", width=150)
        self.tree.column("telephone", width=100)
        self.tree.column("categorie", width=100)
        self.tree.column("employes", width=120)
        self.tree.column("cout_ht", width=100)
        self.tree.column("cout_ttc", width=100)

        self.tree.grid(row=6, column=0, columnspan=2)
        
        # Labels pour les statistiques
        self.label_total_clients = tk.Label(self.stat_frame, text="Total Clients : 0", font=("Helvetica", 12))
        self.label_total_clients.grid(row=7, column=0, sticky="w")

        self.label_chiffre_affaire = tk.Label(self.stat_frame, text="Chiffre d'Affaires : 0.00 €", font=("Helvetica", 16, "bold"))
        self.label_chiffre_affaire.grid(row=7, column=1, sticky="e")

        # Afficher les clients et statistiques dès l'ouverture
        self.afficher_clients()
        self.afficher_statistiques()
    
    def ajouter_client(self):
        """Ajoute un nouveau client à la base de données."""
        try:
            nom = self.entry_nom.get()
            email = self.entry_email.get()
            telephone = self.entry_telephone.get()
            categorie = self.entry_categorie.get().capitalize()
            nombre_employes = int(self.entry_employes.get())
            
            
            # Détermination du prix par employé en fonction de la catégorie
            prix_par_employe = 7 if categorie in ["SEO", "Web"] else 5
            # Création d'un objet Client
            client = Client(nom, email, telephone, categorie, nombre_employes, prix_par_employe)

            # Ajout du client à la base de données
            ajouter_client_bd(client)

            # Confirmation visuelle
            messagebox.showinfo("Succès", f"Client {nom} ajouté avec succès.")
            
            # Nettoyage des champs après ajout
            self.entry_nom.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_telephone.delete(0, tk.END)
            self.entry_categorie.delete(0, tk.END)
            self.entry_employes.delete(0, tk.END)
            # Actualiser les statistiques et les clients après ajout d'un client
            self.afficher_clients()
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide pour le nombre d'employés.")

       
    def afficher_statistiques(self):
        """Affiche et met à jour les statistiques sur les clients."""
        clients = recuperer_clients_bd()
        total_clients = len(clients)
        chiffre_affaire = sum(client[7] for client in clients)

        # Mise à jour des labels de statistiques
        self.label_total_clients.config(text=f"Total Clients : {total_clients}")
        self.label_chiffre_affaire.config(text=f"Chiffre d'Affaires : {chiffre_affaire:.2f} €")

    def afficher_clients(self):
        """Affiche les clients existants dans la base de données dans le Treeview."""
        # Supprimer les anciennes lignes du Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Récupérer les clients depuis la base de données
        clients = recuperer_clients_bd()
        for client in clients:
            self.tree.insert("", "end", values=(client[1], client[2], client[3], client[4], client[5], f"{client[6]:.2f} €", f"{client[7]:.2f} €"))


# Lancement de l'application
if __name__ == "__main__":
    # Création de la base de données si elle n'existe pas
    creer_table_clients()
    
    # Création de l'interface graphique Tkinter
    root = tk.Tk()
    app = CRMApp(root)
    root.mainloop()
