from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('listaProductos/', views.lista_productos, name='lista_productos'),
    path('nuevo_producto/',views.nuevoProducto, name='nuevoProducto'),
    path('editar_producto/<int:pk>/',views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:pk>/',views.eliminar_producto, name='eliminar_producto')
]
