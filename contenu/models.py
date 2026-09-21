from django.db import models

class ContenuSite(models.Model):
    nom_site = models.CharField(max_length=120, default="AGRI-VICTOIRE")
    slogan = models.CharField(max_length=255, default="Des produits agricoles frais, directement du producteur.")
    texte_a_propos = models.TextField(default="AGRI-VICTOIRE est une plateforme de publication et de commande de produits agricoles.")
    image_entete = models.ImageField(upload_to="site/", blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)

    def __str__(self):
        return self.nom_site
