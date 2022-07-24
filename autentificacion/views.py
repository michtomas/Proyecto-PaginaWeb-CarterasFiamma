from django.shortcuts import render, redirect
from django.urls import is_valid_path
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class Registro(View):
    def get(self, request):
        form=UserCreationForm()
        return render(request, 'autentificacion/autentificacion.html', {'form':form})
    
    def post(self,request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'autentificacion/autentificacion.html', {'form':form})


def cerrar_sesion(request):
    logout(request)
    return redirect('Home')
    

def loggear(request):
    if request.method=='POST': #si apretaste el boton
        form=AuthenticationForm(request,data=request.POST) #guardar con los datos
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get('username') #obtener el username
            contraseña=form.cleaned_data.get('password')
            #ahora debemos verificar que el nombre y la contraseña coincidan con alguna de la base de datos, debemos iomportar el authenticated
            usuario=authenticate(username=nombre_usuario, password=contraseña)
            if usuario is not None:
                login(request,usuario)
                return redirect('Home')
            else:
                messages.error(request, 'Usuario no valido')
        else:
            messages.error(request, 'Usuario no valido')
    form=AuthenticationForm()
    return render(request, 'login/login.html', {'form':form})