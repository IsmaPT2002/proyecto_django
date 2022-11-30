
from django.contrib import admin
from django.urls import path, include

from misitio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ("", views.clientes_list, name="clientes_list"),
    path ("clientes/new", views.clientes_list, name="clientes_new"),
]