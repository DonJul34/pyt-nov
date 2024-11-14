import paramiko

# Connexion à un serveur distant via SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("hostname", username="user", password="password")

# Exécution d'une commande sur le serveur
stdin, stdout, stderr = client.exec_command("ls -l /var/log")
print(stdout.read().decode())
client.close()
