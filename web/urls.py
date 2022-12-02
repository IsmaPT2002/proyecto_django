
from django.contrib import admin
from django.urls import path, include

from misitio import views

urlpatterns = [
    path ("clientes", views.clientes_list, name="clientes_lista"),
    path ("clientes/altas", views.clientes_altas, name="clientes_altas"),
    path ("clientes/bajas", views.clientes_bajas, name="clientes_bajas"),
]