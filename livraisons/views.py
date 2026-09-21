from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from commandes.models import Commande
from .models import Livraison

@login_required
def informations_livraison(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id, client=request.user)
    livraison, _ = Livraison.objects.get_or_create(commande=commande, defaults={"nom_complet": request.user.get_full_name() or request.user.username, "telephone": "", "adresse": "", "ville": "", "quartier": ""})
    if request.method == "POST":
        livraison.nom_complet = request.POST.get("nom_complet", "")
        livraison.telephone = request.POST.get("telephone", "")
        livraison.adresse = request.POST.get("adresse", "")
        livraison.ville = request.POST.get("ville", "")
        livraison.quartier = request.POST.get("quartier", "")
        livraison.indications = request.POST.get("indications", "")
        livraison.save()
        return redirect("mes_commandes")
    return render(request, "pages/livraison.html", {"commande": commande, "livraison": livraison})
