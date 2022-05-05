from django.shortcuts import render
from Servicios.models import servicio

# Create your views here.

def servicios(request):
    servicios  = servicio.objects.all()
    return render(request,'Servicios/servicios.html', {'servicios':servicios})
