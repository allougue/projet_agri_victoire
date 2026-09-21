from django.urls import path
from . import views
urlpatterns = [path("a_propos/", views.a_propos, name="a_propos")]
