from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm, CompraForm, BusquedaForm
from django.contrib import messages



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

def realizarCompra(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        #Procesar formulario de compra
        form = CompraForm(request.POST)
        if form.is_valid():
            #Crear la orden de compra:
            importe = form.cleaned_data['importe']
            unidades = form.cleaned_data['unidades']
            fecha = form.cleaned_data['fecha']
            user =   form.cleaned_data['user']
            producto = form.cleaned_data['producto']

            # Redirigir a página de confirmación
            #return redirect('confirmar_compra', orden_de_compra_id=orden_de_compra.id)
            return redirect('lista_productos')
        else:
            messages.error(request, 'Por favor corrija los errores.')
    else:
        form = CompraForm()

    context = {'producto': producto, 'form': form}
    return render(request, 'tienda/realizar_compra.html', context)


def compra(request):
    form = BusquedaForm(request.POST)
    # obtener todos los productos
    productos = Producto.objects.all()
    if request.method == "POST":
        if form.is_valid():
            nombreBuscar = form.cleaned_data['nombre']
            # filtrar productos por nombre de búsqueda
            productos = productos.filter(nombre__icontains=nombreBuscar)
            if productos.count() == 0:
                messages.error(request, 'El producto no se encuentra registrado.')

    return render(request, 'tienda/listaParaComprar.html', {'listaProductos': productos, 'form': form})



















