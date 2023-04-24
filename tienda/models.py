from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    unidades = models.IntegerField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    detalles = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)


class Compra:
    importe = models.DecimalField(max_digits=6, decimal_places=2)
    unidades = models.IntegerField()
    fecha = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)


#class Item_Compra:
 #   producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
  #  compra = models.ForeignKey(Compra, on_delete=models.CASCADE)

