from django.db import models
from django.contrib.auth import get_user_model
from Tienda.models import producto
from django.db.models import F, Sum, FloatField

# Create your models here.
User = get_user_model()
class pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    @property

    def total(self):
        return self.linea_pedido_set.aggregate(
            total = Sum(F("precio")*F("cantidad"), output_field = FloatField())
        )["total"]

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']

class linea_pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(producto, on_delete=models.CASCADE)
    pedido_id = models.ForeignKey(pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto_id.nombre}'
    
    class Meta:
        db_table = 'linea_pedidos'
        verbose_name = 'linea_pedido'
        verbose_name_plural = 'lineas_pedidos'
        ordering = ['id']