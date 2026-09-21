from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import Profil

def inscription(request):
    if request.user.is_authenticated:
        return redirect("accueil")
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        if not username or not password:
            messages.error(request, "Le nom d'utilisateur et le mot de passe sont obligatoires.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur existe déjà.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            Profil.objects.create(utilisateur=user)
            login(request, user)
            return redirect("accueil")
    return render(request, "pages/inscription.html")

def connexion(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        if user:
            login(request, user)
            return redirect(request.GET.get("next", "accueil"))
        messages.error(request, "Identifiants incorrects.")
    return render(request, "pages/connexion.html")

def deconnexion(request):
    logout(request)
    return redirect("accueil")

@login_required
def profil(request):
    profil_obj, _ = Profil.objects.get_or_create(utilisateur=request.user)
    if request.method == "POST":
        request.user.first_name = request.POST.get("first_name", "")
        request.user.last_name = request.POST.get("last_name", "")
        request.user.email = request.POST.get("email", "")
        request.user.save()
        profil_obj.telephone = request.POST.get("telephone", "")
        profil_obj.adresse = request.POST.get("adresse", "")
        profil_obj.ville = request.POST.get("ville", "")
        if request.FILES.get("photo"):
            profil_obj.photo = request.FILES["photo"]
        profil_obj.save()
        messages.success(request, "Profil mis à jour.")
        return redirect("profil")
    return render(request, "pages/profil.html", {"profil": profil_obj})
