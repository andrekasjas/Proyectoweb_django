from django.urls import path
from .views import *


urlpatterns = [
    path('', registro.as_view(), name="autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('logear', logear, name="logear"),
]