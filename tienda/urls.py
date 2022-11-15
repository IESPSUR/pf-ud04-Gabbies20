from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('muestraProductos/',views.muestraProductos,name='muestraProductos'),
    path('agregar/',views.agregar, name = 'agregar'),
    path('eliminar/<str:nombre>/' ,views.eliminar, name='eliminar'),
]
