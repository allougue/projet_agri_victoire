from django.contrib.auth.models import User
from django.db import models
from produits.models import Produit

class Avis(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="avis")
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="avis")
    note = models.PositiveSmallIntegerField()
    commentaire = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.note}/5 - {self.produit.nom}"

    def save(self, *args, **kwargs):
        self.note = max(1, min(5, self.note))
        super().save(*args, **kwargs)
