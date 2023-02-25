from misitio.models import Cliente
from django.shortcuts import render, redirect, get_object_or_404
from misitio.forms import ClienteBajaForm, ClienteForm
from django.contrib import messages


def clientes_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes_lista.html', {'clientes': clientes})

from django.db.models import Q

def clientes_bajas(request):
    mensaje = None
    if request.method == 'POST':
        dni_apellidos = request.POST.get('dni_apellidos', '').strip()
        opcion = request.POST.get('opcion', '')
        if dni_apellidos:
            if opcion == 'dni':
                clientes = Cliente.objects.filter(dni=dni_apellidos)
            elif opcion == 'apellidos':
                clientes = Cliente.objects.filter(apellidos__icontains=dni_apellidos)
            else:
                clientes = None
            if clientes:
                clientes.delete()
                mensaje = 'El cliente ha sido dado de baja correctamente'
            else:
                mensaje = 'No se encontró ningún cliente con el DNI o apellidos proporcionados'
        else:
            mensaje = 'Debe ingresar el DNI o apellidos del cliente'
    return render(request, 'clientes_bajas.html', {'mensaje': mensaje})



def clientes_altas(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente dado de alta correctamente')
            return redirect('clientes_altas')
    else:
        form = ClienteForm()
    return render(request, 'clientes_altas.html', {'form': form})


def instalaciones_list(request):
    return render(request, 'instalaciones.html', {})


def precios_list(request):
    return render(request, 'precios.html', {})


def contacto_list(request):
    return render(request, 'contacto.html', {})
