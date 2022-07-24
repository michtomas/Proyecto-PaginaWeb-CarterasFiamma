from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=20)
    creacion=models.DateTimeField(auto_now_add=True)
    actualizacion=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=20)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='mediaTienda', null=True, blank=True)
    precio=models.FloatField()
    descripcion=models.TextField()
    color=models.CharField(max_length=20)
    disponibilidad=models.BooleanField(default=True)
    creacion=models.DateTimeField(auto_now_add=True)
    actualizacion=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre