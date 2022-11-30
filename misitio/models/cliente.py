from django.db import models

class Cliente(models.Model):
    dni = models.CharField(max_length=10, primary_key= True)
    nombre = models.CharField(max_length=150, blank= False, null= False)
    apellidos = models.CharField(max_length=150, blank= False, null= False)
    fecha_alta = models.DateTimeField('Fecha Alta', blank= False, null= False)
    direccion = models.CharField(max_length=150, blank= False, null= True)
    movil = models.CharField(max_length=150, blank= False, null= True)
    email = models.CharField(max_length=150, blank= False, null= True)

    class Tarifas(models.TextChoices):
        BRONCE = 'BR', 'Bronce'
        PLATA = 'PL', 'Plata'
        ORO = 'OR', 'Oro'
        DIAMANTE = 'DI', 'Diamante'

    tarifa = models.CharField(
        max_length=2,
        choices=Tarifas.choices,
        default=Tarifas.BRONCE,
    )