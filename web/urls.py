
from django.contrib import admin
from django.urls import path, include

from misitio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("clientes/new", views.cliente_new, name="clientes_new"),
    path ("clientes", views.clientes_list, name="clientes_list"),
]