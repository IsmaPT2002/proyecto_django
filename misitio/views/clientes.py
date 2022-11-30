from django.shortcuts import render

from misitio.models import Cliente


def clientes_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes_list.html', {'clientes': clientes})


def clientes_new(request):
    return render(request, 'clientes_new.html', {})
