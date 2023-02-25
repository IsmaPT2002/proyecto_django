from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['dni', 'nombre', 'apellidos', 'fecha_alta', 'direccion', 'movil', 'email', 'tarifa']
class ClienteBajaForm(forms.Form):
    dni = forms.CharField(max_length=10, required=False)
    nombre = forms.CharField(max_length=150, required=False)
    apellidos = forms.CharField(max_length=150, required=False)
