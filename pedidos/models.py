from tabnanny import verbose
from django.db import models

from TiendaOnline.models import Producto


# Create your models here.
class Pedido(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    telefeno=models.IntegerField()
    email=models.EmailField()
    provincia=models.CharField(max_length=20) #hacer un choices
    localidad=models.CharField(max_length=20) 
    
    created_at=models.DateTimeField(auto_now_add=True)
    #clase meta para moldear como se vera la tabla de la base de datos


    class Meta:
        db_table='pedidos'
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering=['id']

