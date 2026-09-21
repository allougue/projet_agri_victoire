from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("utilisateurs.urls")),
    path("", include("produits.urls")),
    path("", include("panier.urls")),
    path("", include("commandes.urls")),
    path("", include("livraisons.urls")),
    path("", include("avis.urls")),
    path("", include("contenu.urls")),
    path("", include("tableau_de_bord.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
