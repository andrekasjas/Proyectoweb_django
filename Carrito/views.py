from django.shortcuts import redirect
from .carrito import Carrito
from Tienda.models import producto

# Create your views here.

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    product = producto.objects.get(id = producto_id)
    carrito.agregar(producto = product)
    return redirect('tienda')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    product = producto.objects.get(id = producto_id)
    carrito.eliminar(producto = product)
    return redirect('tienda')

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    product = producto.objects.get(id = producto_id)
    carrito.restar(producto = product)
    return redirect('tienda')

def vaciar_carrito(request):
    carrito = Carrito(request)
    carrito.vaciar()
    return redirect('tienda')