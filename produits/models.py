from django.contrib.auth.models import User
from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="categories/", blank=True, null=True)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    STATUTS = [
        ("brouillon", "Brouillon"),
        ("publie", "Publié"),
        ("epuise", "Épuisé"),
    ]
    vendeur = models.ForeignKey(User, on_delete=models.CASCADE, related_name="produits")
    nom = models.CharField(max_length=180)
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT, related_name="produits")
    description = models.TextField()
    prix = models.DecimalField(max_digits=12, decimal_places=2)
    unite = models.CharField(max_length=50, default="kg")
    stock = models.PositiveIntegerField(default=0)
    image_principale = models.ImageField(upload_to="produits/")
    date_recolte = models.DateField(blank=True, null=True)
    disponible = models.BooleanField(default=True)
    statut = models.CharField(max_length=20, choices=STATUTS, default="publie")
    date_publication = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom
