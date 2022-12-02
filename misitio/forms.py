from django import forms
from .models import Cliente

class AltaSocioForm(forms.Form):

    dni = forms.Field(label='DNI', max_length=8)
    nombre = forms.Field(label='Nombre', max_length=50)
    apellido = forms.Field(label='Apellido', max_length=50)
    direccion = forms.Field(label='Direccion', max_length=50)
    movil = forms.Field(label='Movil', max_length=50)
    email = forms.Field(label='Email', max_length=50)
