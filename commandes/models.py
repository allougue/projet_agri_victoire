from django.contrib.auth.models import User
from django.db import models
from produits.models import Produit

class Commande(models.Model):
    STATUTS = [
        ("en_attente", "En attente"),
        ("confirmee", "Confirmée"),
        ("preparation", "En préparation"),
        ("livraison", "En livraison"),
        ("livree", "Livrée"),
        ("annulee", "Annulée"),
    ]
    client = models.ForeignKey(User, on_delete=models.PROTECT, related_name="commandes")
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    statut = models.CharField(max_length=20, choices=STATUTS, default="en_attente")
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande #{self.pk}"

class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name="lignes")
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=12, decimal_places=2)
    sous_total = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.produit.nom} x {self.quantite}"
