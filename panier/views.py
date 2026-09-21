from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Panier, LignePanier
from produits.models import Produit

@login_required
def voir_panier(request):
    panier, _ = Panier.objects.get_or_create(client=request.user)
    return render(request, "pages/panier.html", {"panier": panier})

@login_required
def ajouter_au_panier(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id, disponible=True, statut="publie")
    panier, _ = Panier.objects.get_or_create(client=request.user)
    ligne, created = LignePanier.objects.get_or_create(panier=panier, produit=produit)
    if not created:
        ligne.quantite += 1
    ligne.quantite = min(ligne.quantite, produit.stock)
    ligne.save()
    messages.success(request, f"{produit.nom} a été ajouté au panier.")
    return redirect("voir_panier")

@login_required
def modifier_ligne(request, ligne_id):
    panier, _ = Panier.objects.get_or_create(client=request.user)
    ligne = get_object_or_404(LignePanier, id=ligne_id, panier=panier)
    if request.method == "POST":
        quantite = max(1, int(request.POST.get("quantite", 1)))
        ligne.quantite = min(quantite, ligne.produit.stock)
        ligne.save()
    return redirect("voir_panier")

@login_required
def supprimer_ligne(request, ligne_id):
    panier, _ = Panier.objects.get_or_create(client=request.user)
    ligne = get_object_or_404(LignePanier, id=ligne_id, panier=panier)
    ligne.delete()
    return redirect("voir_panier")
