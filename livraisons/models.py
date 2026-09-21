from django.db import models
from commandes.models import Commande

class Livraison(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE, related_name="livraison")
    nom_complet = models.CharField(max_length=180)
    telephone = models.CharField(max_length=30)
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    indications = models.TextField(blank=True)
    date_livraison = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Livraison de {self.nom_complet} - commande #{self.commande_id}"
