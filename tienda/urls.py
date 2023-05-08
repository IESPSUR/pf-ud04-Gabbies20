from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('listaProductos/', views.lista_productos, name='lista_productos'),
    path('nuevo_producto/',views.nuevoProducto, name='nuevoProducto'),
    path('editar_producto/<int:pk>/',views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:pk>/',views.eliminar_producto, name='eliminar_producto'),
    path('realizar_compra/<int:pk>/', views.realizar_compra, name='realizar_compra'),
    path('busqueda/',views.busqueda, name="busqueda"),
    #path('busqueda/',views.busquedaProducto, name="busqueda")
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout_usr'),
    path('salida/', views.salida, name='salida'),
    path('informes/', views.informes, name='informes'),
    path('top10/', views.top_10, name='top10'),
    path('listadoMarca/',views.listadoMarca, name="listadoMarca"),
    path('productosPorUsuario/',views.productosPorUsuario, name="productosPorUsuario"),
    path('top_clientes/', views.top_clientes, name='top_clientes'),
]

