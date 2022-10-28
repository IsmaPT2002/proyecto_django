from django.shortcuts import render

from misitio.forms import ClienteForm
from misitio.models import Cliente


def clientes_list(resquest):
    clientes = Cliente.objects.all()
    return render(resquest, 'misitio/clientes_list.html', {'clientes': clientes})

def cliente_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            cliente.save()
    else:
        form = ClienteForm()
    return render(request, 'misitio/clientes_new.html', {'form': form})