from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from .models import Commande, LigneCommande
from panier.models import Panier

@login_required
@transaction.atomic
def passer_commande(request):
    if request.method != "POST":
        return redirect("voir_panier")
    panier = get_object_or_404(Panier, client=request.user)
    lignes = list(panier.lignes.select_related("produit"))
    if not lignes:
        messages.error(request, "Votre panier est vide.")
        return redirect("voir_panier")
    for ligne in lignes:
        if ligne.quantite > ligne.produit.stock:
            messages.error(request, f"Stock insuffisant pour {ligne.produit.nom}.")
            return redirect("voir_panier")
    commande = Commande.objects.create(client=request.user)
    total = 0
    for ligne in lignes:
        sous_total = ligne.produit.prix * ligne.quantite
        LigneCommande.objects.create(
            commande=commande,
            produit=ligne.produit,
            quantite=ligne.quantite,
            prix_unitaire=ligne.produit.prix,
            sous_total=sous_total,
        )
        ligne.produit.stock -= ligne.quantite
        if ligne.produit.stock == 0:
            ligne.produit.disponible = False
            ligne.produit.statut = "epuise"
        ligne.produit.save()
        total += sous_total
    commande.total = total
    commande.save()
    panier.lignes.all().delete()
    messages.success(request, "Votre commande a été enregistrée. Aucun paiement en ligne n'est demandé.")
    return redirect("mes_commandes")

@login_required
def mes_commandes(request):
    commandes = Commande.objects.filter(client=request.user).prefetch_related("lignes__produit")
    return render(request, "pages/mes_commandes.html", {"commandes": commandes})

@login_required
def commandes_producteur(request):
    if not request.user.is_staff:
        return redirect("accueil")
    commandes = Commande.objects.filter(lignes__produit__vendeur=request.user).distinct().prefetch_related("lignes__produit")
    return render(request, "pages/commandes_producteur.html", {"commandes": commandes})

@login_required
def modifier_statut_commande(request, commande_id):
    if not request.user.is_staff or request.method != "POST":
        return redirect("commandes_producteur")
    commande = get_object_or_404(Commande, id=commande_id)
    statut = request.POST.get("statut")
    if statut in dict(Commande.STATUTS):
        commande.statut = statut
        commande.save()
    return redirect("commandes_producteur")
