from django.contrib.auth.models import User
from django.db import models

class Profil(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profil")
    telephone = models.CharField(max_length=30, blank=True)
    adresse = models.CharField(max_length=255, blank=True)
    ville = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to="profils/", blank=True, null=True)

    def __str__(self):
        return self.utilisateur.get_full_name() or self.utilisateur.username
