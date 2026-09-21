from django.urls import path
from . import views
urlpatterns = [
            path("tableau_de_bord/", views.tableau_de_bord, name="tableau_de_bord"),
            path('inscription/', views.inscription_view, name='inscription'),
            path('connexion/', views.connexion_view, name='connexion'),
            path('deconnexion/', views.deconnexion_view, name='deconnexion'),

               ]
