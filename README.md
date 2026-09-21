# AGRI-VICTOIRE

Plateforme Django de publication et de commande de produits agricoles.

## Technologies
- Python
- Django
- SQLite (base de données par défaut)
- Tailwind CSS via CDN pour le prototype
- JavaScript
- Lucide Icons via CDN
- Chart.js via CDN

## Applications Django
- utilisateurs : inscription, connexion et profils
- produits : catégories, publication et gestion du stock
- panier : panier du client
- commandes : création et suivi des commandes
- livraisons : informations de livraison
- avis : notes et commentaires
- contenu : contenu de la navigation et de la page À propos
- tableau_de_bord : statistiques du producteur et de l'administrateur

## Installation
```bash
python -m venv virtuel
virtuel\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Ouvrir http://127.0.0.1:8000/

## Tailwind
Le prototype utilise Tailwind CSS par CDN pour démarrer rapidement dans VS Code. Pour une mise en production, Tailwind peut ensuite être compilé localement avec Node.js.

## Publication
Un seul compte producteur peut publier les produits. Dans Django Admin, donne au compte producteur le statut `is_staff=True`. Les autres utilisateurs restent clients.

## À propos
Les contenus de la page À propos et l'image d'en-tête sont modifiables depuis Django Admin via l'application `contenu`.
