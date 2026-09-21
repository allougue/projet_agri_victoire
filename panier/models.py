from django.contrib.auth.models import User
from django.db import models
from produits.models import Produit

class Panier(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE, related_name="panier")
    date_creation = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return sum(ligne.sous_total for ligne in self.lignes.select_related("produit"))

class LignePanier(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE, related_name="lignes")
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("panier", "produit")

    @property
    def sous_total(self):
        return self.produit.prix * self.quantite
