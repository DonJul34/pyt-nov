def calculer_facture(prix,quantity,taux_tva=0.20):
    montant_ttc = prix * quantity * (1+taux_tva)
    return montant_ttc

facture = calculer_facture(100,5,0.30)

print(f"Montant total TTC : {facture} €")  # Affiche "Montant total TTC : 600.0 €"

def rechercher_client(**kwargs):
    print("\nInformation du client")
    for cle, valeur in kwargs.items():
        print(f"{cle.capitalize()} : {valeur}")
        print(f"{cle.upper()} : {valeur}")

        
rechercher_client(nom="Alice", email="alice@example.com", telephone="123456789", age="22",notes="18/20",professeur_principal="Monsieur lafèbrevre")

produit = lambda x,y : x * y
resultat = produit(4,5)
print(f"Le produit des deux nombres est : {resultat}")  # Affiche "Le produit des deux nombres est : 20"
