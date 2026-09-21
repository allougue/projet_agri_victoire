from django.contrib import admin
from .models import Categorie, Produit

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ("nom",)
    search_fields = ("nom",)

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ("nom", "categorie", "prix", "stock", "disponible", "statut", "date_publication")
    list_filter = ("categorie", "disponible", "statut")
    search_fields = ("nom", "description")
    readonly_fields = ("date_publication", "date_modification")
