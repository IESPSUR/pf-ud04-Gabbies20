from django.shortcuts import render,redirect
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



def eliminar(request, nombre): #Acptamos un parametro el ID del producto que vamos a eliminar
    #Buscamos esa producto en nuestro modelo:
    producto = Producto.objects.get(id=nombre)
    producto.delete()
    return redirect('muestraProductos', {'producto':producto})

#def editar(request, producto_id):
 #   producto=Producto.objects.get(id=producto_id)
  #  if request.method == "POST":
   #     form= ProductoForm(request.POST,instance=producto)
    #    if form.is_valid():
     #       form.save()
      #      return redirect("muestraProductos")
    #else:
     #   form = ProductoForm(instance=producto)
    #context = {'form': form}
    #return render(request, 'tienda/editar.html', context)
