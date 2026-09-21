from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Avis
from produits.models import Produit

@login_required
def ajouter_avis(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == "POST":
        Avis.objects.update_or_create(
            client=request.user, produit=produit,
            defaults={"note": request.POST.get("note", 5), "commentaire": request.POST.get("commentaire", "")}
        )
    return redirect("detail_produit", produit_id=produit.id)
