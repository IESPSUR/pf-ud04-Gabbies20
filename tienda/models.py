import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=20, primary_key=True)
class Producto(models.Model):
    marca_producto= models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20, primary_key=True)
    modelo = models.CharField(max_length=20)
    unidades = models.IntegerField()
    precio = models.FloatField()
    detalles = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
class Compra(models.Model):
    nombre_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha =models.DateTimeField(default=timezone.now)
    unidades =models.IntegerField()
    importe = models.FloatField()


