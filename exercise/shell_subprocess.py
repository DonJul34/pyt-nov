import psutil
import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurer les seuils d'alerte
CPU_THRESHOLD = 80  # En pourcentage
MEMORY_THRESHOLD = 80  # En pourcentage
DISK_THRESHOLD = 80  # En pourcentage

# Configuration de l'email d'alerte
SENDER_EMAIL = "votre_email@example.com"
RECEIVER_EMAIL = "destinataire@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "votre_email@example.com"
SMTP_PASSWORD = "votre_mot_de_passe"

def check_system_resources():
    # Récupération de l'utilisation des ressources
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    
    # Préparation du message d'alerte si un seuil est dépassé
    alerts = []
    if cpu_usage > CPU_THRESHOLD:
        alerts.append(f"CPU usage is high: {cpu_usage}%")
    if memory_usage > MEMORY_THRESHOLD:
        alerts.append(f"Memory usage is high: {memory_usage}%")
    if disk_usage > DISK_THRESHOLD:
        alerts.append(f"Disk usage is high: {disk_usage}%")
    
    # Envoi d'un email si des alertes existent
    if alerts:
        send_alert_email(alerts)

def send_alert_email(alerts):
    # Configuration de l'email
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL
    message["Subject"] = "Alerte de Surveillance des Ressources Système"
    alert_message = "\n".join(alerts)
    message.attach(MIMEText(alert_message, "plain"))

    # Envoi de l'email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
        print("Email d'alerte envoyé avec succès")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")

# Planification de la vérification toutes les 5 minutes
schedule.every(5).minutes.do(check_system_resources)

print("Surveillance des ressources système lancée...")
while True:
    schedule.run_pending()
    time.sleep(1)
