from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):


    #La clase meta le dice a la clase ProductoFrom como comportarse
    class Meta:
        #Estamos haciendo model con el modelo de models.py,para poder usar nuestro fromulario
        #debemos ir a views,py e importarlo.
        model = Producto
        fields = ['nombre','marca_producto','modelo','unidades','precio','detalles']