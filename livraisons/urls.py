from django.urls import path
from . import views
urlpatterns = [
    path("livraison/<int:commande_id>/", views.informations_livraison, name="informations_livraison"),
]
