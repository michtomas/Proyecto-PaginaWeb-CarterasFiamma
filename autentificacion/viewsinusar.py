from django.contrib.auth import forms 
from django.shortcuts import redirect, render  
from django.contrib.auth import login
from django.contrib import messages  
from django.contrib.auth.forms import UserCreationForm  
from .forms import CustomUserCreationForm  
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect
# Create your views here.  

class Registro(View):
    def get(self, request):
        form=CustomUserCreationForm()
        return render(request, 'autentificacion/autentificacion.html',{'form':form})

    @csrf_protect
    def post(self, request):  
        if request.POST == 'POST':  
            form = CustomUserCreationForm()  
            if form.is_valid():  
                usuario=form.save()  
                login(request, usuario)
                return redirect('Home')
        else:  
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'autentificacion/autentificacion.html', context)  
            