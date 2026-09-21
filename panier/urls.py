from django.urls import path
from . import views

urlpatterns = [
    path("panier/", views.voir_panier, name="voir_panier"),
    path("ajouter_au_panier/<int:produit_id>/", views.ajouter_au_panier, name="ajouter_au_panier"),
    path("modifier_ligne/<int:ligne_id>/", views.modifier_ligne, name="modifier_ligne"),
    path("supprimer_ligne/<int:ligne_id>/", views.supprimer_ligne, name="supprimer_ligne"),
]
