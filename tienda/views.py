from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Compra, Marca
from .forms import ProductoForm, CompraForm, BusquedaForm, IniciarSesionForm
from django.contrib import messages
from django.db import transaction
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.db.models import Sum


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

"""
def realizarCompra(request,pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto = Producto.objects.get(id=pk)

    if request.method == 'POST':
        # Obtener los datos del formulario
        unidades = request.POST['unidades']
        importe = request.POST['importe']

        # Crear una instancia de Compra
        compra = Compra(
            producto=producto,
            unidades=unidades,
            importe=importe,
            user=request.user
        )

        # Guardar la compra en la base de datos
        compra.save()

            # Redirigir a página de confirmación
            #return redirect('confirmar_compra', orden_de_compra_id=orden_de_compra.id)
            #return redirect('lista_productos')
        #else:
            #messages.error(request, 'Por favor corrija los errores.')
    else:
        form = CompraForm()

        context = {'producto': producto, 'form': form}
    return render(request, 'tienda/realizar_compra.html', context)

"""

def busqueda(request):
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



#@login_required
def realizar_compra(request, pk):
    # Obtener el producto correspondiente a la clave primaria pk
    producto = get_object_or_404(Producto, pk=pk)

    # Crear una instancia del formulario de compra
    form = CompraForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # Obtener el número de unidades a comprar del formulario
        num_unidades = form.cleaned_data['unidades']
        importe= producto.precio * (num_unidades)

        # Crear una instancia de la compra
        compra = Compra(user=request.user,producto=producto, unidades=num_unidades, importe=importe, fecha=datetime.today())
        compra.save()

        # Restar las unidades compradas del producto
        producto.unidades -= num_unidades
        producto.save()

        # Mostrar un mensaje de éxito
        messages.success(request, 'Compra realizada con éxito.')

        # Redirigir al usuario a la página de inicio
        return redirect(salida)

    context = {'producto': producto, 'form': form}
    return render(request, 'tienda/realizar_compra.html', context)

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('welcome')
    else:
        form = UserCreationForm()
    return render(request, 'tienda/registro.html', {'form': form})



#def login(request):
    """Logeo de usuario ya creado"""
 #   if request.method == "POST":
  #      form = AuthenticationForm(request, data=request.POST)
   #     if form.is_valid():
    #        username = form.cleaned_data.get('username')
     #       password = form.cleaned_data.get('password')
      #      user = authenticate(username=username, password=password)
       #     if user is not None:
        #        login(request,user)
         #       return redirect("listado")
          #  else:
           #     messages.error(request, "Error en el inicio de sesión")
        #else:
         #   messages.error(request, "Fallo en el inicio de sesión")
    #form = AuthenticationForm()
    #return render(request, "tienda/login.html", {'login_form':form})






def iniciar_sesion(request):
    if request.method == 'POST':
        form = IniciarSesionForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('salida')
    else:
        form = AuthenticationForm()
    return render(request, 'tienda/login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('login')


def salida(request):
    return render(request,'tienda/salida.html', {})


def informes(request):
    marcas = Marca.objects.all()
    return render(request, 'tienda/informes.html',{})



def top_10(request):
    ventas = Compra.objects.values('producto').annotate(total_unidades=Sum('unidades')).order_by('-total_unidades')[:10]
    productos = []
    for venta in ventas:
        producto = Producto.objects.get(pk=venta['producto'])
        productos.append({'producto': producto.nombre, 'unidades': venta['total_unidades']})
    return render(request, 'tienda/top_10.html', {'productos': productos})

#Primero, se usa values para agrupar las ventas por producto y annotate con Sum para obtener la suma de unidades vendidas para cada producto. Luego, se ordena la lista de ventas de mayor a menor y se toman los 10 primeros con [:10].
#Luego, se crea una lista productos vacía y se itera sobre la lista de ventas para obtener el objeto Producto correspondiente a cada venta. Con el objeto Producto, se crea un diccionario con el nombre del producto y la cantidad total vendida y se agrega a la lista productos.
#Finalmente, se renderiza la plantilla tienda/top_10.html con la lista productos. En la plantilla, se puede acceder al nombre del producto con {{ producto.nombre }} y a la cantidad total vendida con {{ producto.unidades }}


def listadoMarca(request):
    marcas = Marca.objects.all()
    return render(request, 'tienda/productosPorMarca.html', {'marcas': marcas})


def productosPorUsuario(request):
    usuarios = User.objects.all()
    productos_por_usuario = []

    for usuario in usuarios:
        ventas = Compra.objects.filter(user_id=usuario.id)
        total_productos = 0
        for venta in ventas:
            total_productos += venta.unidades
        productos_por_usuario.append({'usuario': usuario.username, 'productos': total_productos})

    return render(request, 'tienda/productosPorUsuario.html', {'productos_por_usuario': productos_por_usuario})


def top_clientes(request):
    clientes = User.objects.annotate(total_gastado=Sum('compra__importe')).order_by('-total_gastado')[:10]
    return render(request, 'tienda/top_clientes.html', {'clientes': clientes})