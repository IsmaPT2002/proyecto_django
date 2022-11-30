
from django.contrib import admin
from django.urls import path, include

from misitio import views

urlpatterns = [
    path ("", views.clientes_list, name="clientes_list"),
    path ("clientes/new", views.clientes_new, name="clientes_new"),
]