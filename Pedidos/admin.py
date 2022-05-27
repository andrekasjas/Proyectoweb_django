from django.contrib import admin
from .models import pedido, linea_pedido

# Register your models here.

class pedido_admin(admin.ModelAdmin):
    readonly_fields=('created_at',)

class linea_pedido_admin(admin.ModelAdmin):
    readonly_fields=('created_at',)

admin.site.register(pedido, pedido_admin)
admin.site.register(linea_pedido, linea_pedido_admin)