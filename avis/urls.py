from django.urls import path
from . import views
urlpatterns = [path("ajouter_avis/<int:produit_id>/", views.ajouter_avis, name="ajouter_avis")]
