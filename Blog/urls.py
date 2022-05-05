from django.urls import path
from .views import *


urlpatterns = [
    path('', blog, name="blog"),
    path('categoria/<int:categoria_id>/', categoria, name="categoria"),
]