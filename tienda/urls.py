from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('muestraProductos/',views.muestraProductos,name='muestraProductos'),
    path('agregar/',views.agregar, name = 'agregar'),
    path('eliminar/<int:pk>/' ,views.eliminar, name='eliminar'),
]
