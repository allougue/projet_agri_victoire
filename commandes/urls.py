from django.urls import path
from . import views

urlpatterns = [
    path("passer_commande/", views.passer_commande, name="passer_commande"),
    path("mes_commandes/", views.mes_commandes, name="mes_commandes"),
    path("commandes_producteur/", views.commandes_producteur, name="commandes_producteur"),
    path("modifier_statut_commande/<int:commande_id>/", views.modifier_statut_commande, name="modifier_statut_commande"),
]
