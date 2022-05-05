from django.urls import path
from .views import *

urlpatterns = [
    path('', contacto, name="contacto"),
]
