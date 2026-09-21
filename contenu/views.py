from django.shortcuts import render
from .models import ContenuSite

def a_propos(request):
    contenu = ContenuSite.objects.first()
    return render(request, "pages/a_propos.html", {"contenu": contenu})
