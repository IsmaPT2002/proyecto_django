from django.shortcuts import render

from misitio.models import Cliente


def clientes_list(resquest):
    clientes = Cliente.objects.all()
    return render(resquest, 'misitio/clientes_list.html', {'clientes': clientes})
