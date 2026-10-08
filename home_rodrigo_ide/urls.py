from django.contrib import admin
from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('peliculas/accion', views.peliculas_accion, name="peliculas_accion"),
    path('peliculas/terror', views.peliculas_terror, name="peliculas_terror")
]
