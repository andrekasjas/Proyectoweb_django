from django.urls import path
from .views import *


urlpatterns = [
    path('', tienda, name="tienda"),
    path('categoria_producto/<int:categoria_producto_id>/', categoria_producto, name="categoria_producto"),
]