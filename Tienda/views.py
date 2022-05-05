from django.shortcuts import render
from .models import producto, categoria_producto

# Create your views here.

def tienda(request):
    productos = producto.objects.all()
    return render(request,'Tienda/tienda.html', {'productos':productos})

def categoria_producto(request, categoria_producto_id):
    categoris = categoria_producto.objects.get(id = categoria_producto_id)
    productos = producto.objects.filter(categoria_producto = categoria_producto_id)
    return render(request, 'Tienda/categoria_producto.html', {"categoris":categoris, "productos":productos})


