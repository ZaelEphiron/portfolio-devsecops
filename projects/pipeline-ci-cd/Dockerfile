# Utilisation d'une image Python officielle et légère
FROM python:3.11-slim

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers du projet dans le conteneur
COPY . .

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande par défaut : exécuter l'application
CMD ["python", "app.py"]
