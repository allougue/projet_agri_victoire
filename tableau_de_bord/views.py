from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import redirect, render
from produits.models import Produit
from commandes.models import Commande
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

@login_required
def tableau_de_bord(request):
    if not request.user.is_staff:
        return redirect("accueil")
    produits = Produit.objects.filter(vendeur=request.user)
    commandes = Commande.objects.filter(lignes__produit__vendeur=request.user).distinct()
    ventes = commandes.filter(statut__in=["confirmee","preparation","livraison","livree"]).aggregate(total=Sum("total"))["total"] or 0
    return render(request, "pages/tableau_de_bord.html", {
        "nombre_produits": produits.count(),
        "nombre_commandes": commandes.count(),
        "stock_total": produits.aggregate(total=Sum("stock"))["total"] or 0,
        "ventes": ventes,
        "commandes": commandes[:8],
    })

@login_required
def profile_view(request):
    if request.method == 'POST':
        # Exemple si vous mettez à jour manuellement ou via un ModelForm :
        profile = request.user.profile
        
        if 'photo' in request.FILES:
            profile.photo = request.FILES['photo']
            
        profile.telephone = request.POST.get('telephone')
        profile.adresse = request.POST.get('adresse')
        profile.ville = request.POST.get('ville')
        profile.save()
        
        # Mettre à jour l'utilisateur de base
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.email = request.POST.get('email')
        request.user.save()

        return redirect('profile')

    return render(request, 'profile.html')

def inscription_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Connecte l'utilisateur après l'inscription
            messages.success(request, "Compte créé avec succès !")
            return redirect('accueil') # Ou la page de votre choix
    else:
        form = UserCreationForm()
    return render(request, 'pages/inscription.html', {'form': form})

def connexion_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accueil')
        messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = AuthenticationForm()
    return render(request, 'pages/connexion.html', {'form': form})

def deconnexion_view(request):
    logout(request)
    return redirect('connexion')