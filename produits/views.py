from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .models import Produit, Categorie
from contenu.models import ContenuSite

def est_producteur(user):
    return user.is_authenticated and user.is_staff

def accueil(request):
    recherche = request.GET.get("recherche", "").strip()
    categorie = request.GET.get("categorie", "")
    tri = request.GET.get("tri", "-date_publication")
    produits = Produit.objects.filter(disponible=True, statut="publie").select_related("categorie", "vendeur")
    if recherche:
        produits = produits.filter(Q(nom__icontains=recherche) | Q(description__icontains=recherche))
    if categorie:
        produits = produits.filter(categorie_id=categorie)
    if tri not in ["-date_publication", "prix", "-prix"]:
        tri = "-date_publication"
    produits = produits.order_by(tri)
    return render(request, "pages/accueil.html", {
        "contenu": ContenuSite.objects.first(),
        "produits": produits,
        "categories": Categorie.objects.all(),
        "recherche": recherche,
        "categorie_active": categorie,
        "tri": tri,
    })

def detail_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id, statut="publie")
    return render(request, "pages/detail_produit.html", {"produit": produit})

@login_required
def ajouter_produit(request):
    if not est_producteur(request.user):
        messages.error(request, "Seul le producteur autorisé peut publier des produits.")
        return redirect("accueil")
    categories = Categorie.objects.all()
    if request.method == "POST":
        categorie = get_object_or_404(Categorie, id=request.POST.get("categorie"))
        Produit.objects.create(
            vendeur=request.user,
            nom=request.POST.get("nom"),
            categorie=categorie,
            description=request.POST.get("description"),
            prix=request.POST.get("prix"),
            unite=request.POST.get("unite"),
            stock=request.POST.get("stock"),
            image_principale=request.FILES.get("image_principale"),
            date_recolte=request.POST.get("date_recolte") or None,
            disponible=bool(request.POST.get("disponible")),
            statut="publie",
        )
        messages.success(request, "Produit publié avec succès.")
        return redirect("mes_produits")
    return render(request, "pages/ajouter_produit.html", {"categories": categories})

@login_required
def mes_produits(request):
    if not est_producteur(request.user):
        return redirect("accueil")
    produits = Produit.objects.filter(vendeur=request.user)
    return render(request, "pages/mes_produits.html", {"produits": produits})

@login_required
def supprimer_produit(request, produit_id):
    if not est_producteur(request.user):
        return redirect("accueil")
    produit = get_object_or_404(Produit, id=produit_id, vendeur=request.user)
    if request.method == "POST":
        produit.delete()
        messages.success(request, "Produit supprimé.")
    return redirect("mes_produits")
