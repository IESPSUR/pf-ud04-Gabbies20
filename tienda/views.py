from django.shortcuts import render,redirect
from .models import Producto
from .forms import ProductoForm



# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "tienda/listaProductos.html", {'productos': productos})


def nuevoProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'tienda/nuevo_producto.html', {'form': form})


def editar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'tienda/editar_producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    producto.delete()
    return redirect('lista_productos')

