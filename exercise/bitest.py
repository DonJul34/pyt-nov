import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import psycopg2
import openai

# Configuration OpenAI
openai.api_key = "VOTRE_CLE_API_OPENAI"

# Connexion à la base de données
conn = psycopg2.connect(
    dbname="votre_bdd",
    user="votre_utilisateur",
    password="votre_mot_de_passe",
    host="localhost"
)
cursor = conn.cursor()

# Configuration de Selenium
driver = webdriver.Chrome(executable_path="path_to_chromedriver")

def scrape_linkedin_company(company_name):
    driver.get("https://www.linkedin.com/")
    time.sleep(2)
    
    # Login LinkedIn (ajoutez vos identifiants)
    username = driver.find_element(By.ID, "session_key")
    password = driver.find_element(By.ID, "session_password")
    username.send_keys("votre_email")
    password.send_keys("votre_mot_de_passe")
    driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button").click()
    time.sleep(2)
    
    # Recherche de l'entreprise
    search_bar = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Rechercher']")
    search_bar.send_keys(company_name)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(2)
    
    # Sélectionner la première entreprise
    companies = driver.find_elements(By.XPATH, "//a[contains(@href, '/company/')]")
    if companies:
        companies[0].click()
    else:
        print(f"Impossible de trouver l'entreprise : {company_name}")
        return None
    time.sleep(3)
    
    # Extraction des informations de l'entreprise
    try:
        name = driver.find_element(By.XPATH, "//h1").text
        description = driver.find_element(By.XPATH, "//section[contains(@class, 'org-top-card-summary')]").text
        secteur = driver.find_element(By.XPATH, "//dd[contains(@class, 'org-page-details__definition-text')][1]").text
        emplacement = driver.find_element(By.XPATH, "//dd[contains(@class, 'org-page-details__definition-text')][2]").text
    except Exception as e:
        print(f"Erreur d'extraction : {e}")
        return None

    # Sauvegarde dans la base de données
    cursor.execute(
        "INSERT INTO entreprises (nom, description, secteur, emplacement) VALUES (%s, %s, %s, %s) RETURNING id",
        (name, description, secteur, emplacement)
    )
    entreprise_id = cursor.fetchone()[0]
    conn.commit()
    
    print(f"Entreprise {name} ajoutée avec l'ID {entreprise_id}.")
    return entreprise_id, description

### Étape 4 : Classification des Entreprises avec OpenAI

Ensuite, utilisons OpenAI pour classer chaque entreprise en fonction de sa description.

def classify_company(description):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Classifie cette entreprise : {description}. Classe dans les catégories suivantes : Technologie, Finance, Santé, Education, Autre.",
        max_tokens=10
    )
    classification = response.choices[0].text.strip()
    return classification

### Étape 5 : Intégration et Exécution

Une fois que les entreprises sont scrappées et stockées, nous les classons automatiquement avec OpenAI.

def process_companies(companies):
    for company in companies:
        entreprise_id, description = scrape_linkedin_company(company)
        if entreprise_id and description:
            classification = classify_company(description)
            cursor.execute(
                "UPDATE entreprises SET classification = %s WHERE id = %s",
                (classification, entreprise_id)
            )
            conn.commit()
            print(f"Entreprise ID {entreprise_id} classée sous {classification}.")

# Liste des entreprises à scraper
companies = ["Google", "Microsoft", "Pfizer", "BNP Paribas", "Harvard University"]
process_companies(companies)

# Fermer la connexion et le navigateur
cursor.close()
conn.close()
driver.quit()
