from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})
def muestraProductos(request):
    producto=Producto.objects.all()
    return render(request,'tienda/listaProductos.html',{'producto':producto})


#Siempre que utilizamos formularios debemos utilizar los 2 tipos de peticiones:
#post y get
def agregar(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            #Tenemos acceso al metodo .save pq estamos asociendo nuestro formulario a
            #un modelo, es la ventaja que nos da tener un modelForm.
            form.save()
            #redirect debo importarlo.
            return redirect('muestraProductos')
    else:
        form = ProductoForm()

    context={'form' : form}
    return render(request,'tienda/agregar.html',context)



def eliminar(request, nombre): #Aceptamos un parametro el ID del producto que vamos a eliminar
    #Buscamos ese producto en nuestro modelo:
    producto = get_object_or_404(Producto, pk=nombre)
    if request.method=='POST':
        producto.delete()
        return redirect('muestraProductos')

def editar(request, nombre):
    producto=Producto.objects.get(nombre)
    if request.method == "POST":
        form= ProductoForm(request.POST,instance=producto)
        if form.is_valid():
            form.save()
            return redirect("muestraProductos")
    #else:
     #   form = ProductoForm(instance=producto)
    #context = {'form': form}
    #return render(request, 'tienda/editar.html', context)
