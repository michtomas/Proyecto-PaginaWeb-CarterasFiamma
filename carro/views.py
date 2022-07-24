from django.shortcuts import render, redirect
from .carro import Carro
from TiendaOnline.models import Producto

# Create your views here.

def agregar_producto(request,id):
    carro=Carro(request)
    producto=Producto.objects.get(id=id)
    carro.agregar_producto(producto=producto)
    return redirect('Tienda') #redireccionar a la tienda


def eliminar_producto(request,id):
    carro=Carro(request)
    producto=Producto.objects.get(id=id)
    carro.eliminar_producto(producto=producto)
    return redirect('Tienda') #redireccionar a la tienda


def vaciar_carrito(request):
    carro=Carro(request)
    carro.vaciar_carro()
    return redirect('Tienda')












