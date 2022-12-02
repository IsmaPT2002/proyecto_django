from django.shortcuts import render

from misitio.models import Cliente


def clientes_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes_lista.html', {'clientes': clientes})


def clientes_altas(request):
    return render(request, 'clientes_altas.html', {})

def clientes_bajas(request):
    return render(request, 'clientes_bajas.html', {})

def altaCliente(request):
    if request.method == 'POST':
        form = AltaSocioForm(request.POST)
        if form.is_valid():
            cliente = Cliente(
                dni=form.cleaned_data['dni'],
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                direccion=form.cleaned_data['direccion'],
                movil=form.cleaned_data['movil'],
                email=form.cleaned_data['email'],
            )
            cliente.save()
            return HttpResponseRedirect('/clientes/lista')
    else:
        form = AltaSocioForm()
    return render(request, 'clientes_altas.html', {'form': form})
def instalaciones_list(request):
    return render(request, 'instalaciones.html', {})

def precios_list(request):
    return render(request, 'precios.html', {})

def contacto_list(request):
    return render(request, 'contacto.html', {})
