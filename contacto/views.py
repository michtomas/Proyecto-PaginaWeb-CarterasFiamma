from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
#importamos el formualario
from .forms import FormularioContacto
# Create your views here.

@csrf_protect
def contacto(request):
    formulario_contacto=FormularioContacto()

    #si hay post queremos recibir la informacion
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST) #cargar en el formulario la informacion introducida
        if formulario_contacto.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            contenido=request.POST.get('contenido')
            return redirect("/contacto/?valido")
            #lyuego de recibir correctamente la informacion del mensaje+
            #queremos enviar un mensaje a la pagina de que el mensaje fue enviado
            #redericcionamos a contacto con un pase de paremetro
        
    return render(request,'contacto/contacto.html',{'formulario_contacto':formulario_contacto})

