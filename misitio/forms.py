from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields =[ 'dni', 'nombre', 'fechalta', 'direccion', 'mobile']

    # también podríamos hacer
    # class Meta:
    #     model = Canciones
    #     fields = '__all__'
