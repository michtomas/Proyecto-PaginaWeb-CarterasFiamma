from django.contrib import admin
from TiendaOnline.models import Categoria,Producto
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    #esto es para la visualizacion en el panel de admin
    list_display=("nombre", "creacion", "actualizacion")
    #esto es para agregar una casilla de busqueda en el panel de admin para los clientes
    search_fields=('nombre','creacion') #busqueda por nombre 

class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre','categoria','precio','color','disponibilidad','creacion','actualizacion')
    search_fields=('nombre','categoria','precio')


admin.site.register(Producto,ProductoAdmin)
admin.site.register(Categoria,CategoriaAdmin)
