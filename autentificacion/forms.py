from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  
  
class CustomUserCreationForm(UserCreationForm):  
    username = forms.CharField(label='Usuario', max_length=20)  
    nombre = forms.CharField(label='Nombre', min_length=5, max_length=20)
    apellido = forms.CharField(label='Apellido', min_length=5, max_length=20)
    telefono = forms.IntegerField(label='Telefono') 
    email = forms.EmailField(label='Email')  
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)  
  
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("El nombre de usuario ya existe")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError("El mail ingresado ya existe")  
        return email  
    
    def tel_clean(self):  
        telefono = self.cleaned_data['telefono'].lower()  
        new = User.objects.filter(telefono=telefono)  
        if new.count():  
            raise ValidationError("El telefono ingresado ya existe")  
        return telefono

    def clean_password2(self):  
        password1 = self.cleaned_data['contraseña1']  
        password2 = self.cleaned_data['contraseña2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Las contraseñas no coinciden")  
        return password2
  
    def save(self, commit = True):  
        usuario = User.objects.create_user(  
            self.cleaned_data['nombre_usuario'],  
            self.cleaned_data['email'],  
            self.cleaned_data['contraseña1'],
            self.cleaned_data['telefono'],
            self.cleaned_data['nombre'],
            self.cleaned_data['apellido'],  
        )  
        return usuario  