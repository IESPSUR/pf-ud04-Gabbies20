from django.shortcuts import render
from .models import Producto

# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})

def muestraProductos(request):
    producto=Producto.objects.all()
    return render(request,'tienda/listaProductos.html',{'producto':producto})