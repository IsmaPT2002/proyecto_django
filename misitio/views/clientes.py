from django.shortcuts import render

from misitio.models import Cliente


def clientes_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes_lista.html', {'clientes': clientes})


def clientes_altas(request):
    return render(request, 'clientes_altas.html', {})

def clientes_bajas(request):
    return render(request, 'clientes_bajas.html', {})
