from django.shortcuts import render, redirect
from .forms import Formulario_contacto
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.

def contacto(request):
    if (request.method == "POST"):
        formulario = Formulario_contacto(data = request.POST)
        if (formulario.is_valid()):
            nombre = request.POST.get('nombre') 
            email = request.POST.get('email') 
            contenido = request.POST.get('contenido') 

            email = EmailMessage('Mensaje enviado desde la app creada en django', 
            'El usuario con nombre {} y direccion {} te informa que:\n\n{}'.format(nombre,email,contenido), 
            '', [settings.EMAIL_HOST_USER], reply_to=[email])

            try:
                email.send()
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?novalido')
    else:
        formulario = Formulario_contacto()

    return render(request, "Contacto/contacto.html",{'formulario':formulario})