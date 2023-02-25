from django.db import models
from django import forms
class Cliente(models.Model):
    dni = models.CharField(max_length=10, primary_key= True)
    nombre = models.CharField(max_length=150, blank= False, null= False)
    apellidos = models.CharField(max_length=150, blank= False, null= False)
    fecha_alta = models.DateTimeField('Fecha Alta', blank= False, null= False)
    direccion = models.CharField(max_length=150, blank= False, null= True)
    movil = models.CharField(max_length=150, blank= False, null= True)
    email = models.CharField(max_length=150, blank= False, null= True)

    class Tarifas(models.TextChoices):
        DESCUENTO = 'DES', 'Descuento(<18, >65 o discapacidad)'
        JOVENES = 'JOV', 'Jovenes(Entre 19 y 25 años)'
        ADULTOS = 'ADU', 'Adultos(Entre 26 y 64 años)'

    tarifa = models.CharField(
        max_length=3,
        choices=Tarifas.choices,
        default=Tarifas.ADULTOS,
    )