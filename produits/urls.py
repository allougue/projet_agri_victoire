from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("produits/<int:produit_id>/", views.detail_produit, name="detail_produit"),
    path("ajouter_produit/", views.ajouter_produit, name="ajouter_produit"),
    path("mes_produits/", views.mes_produits, name="mes_produits"),
    path("supprimer_produit/<int:produit_id>/", views.supprimer_produit, name="supprimer_produit"),
]
