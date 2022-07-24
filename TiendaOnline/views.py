from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Producto #imoprtamos el models de prooducto para poder mostrarlos en el template de la tienda

# Create your views here.
def tienda(request):

    #para mostrar los productos creamos una lista donde almacenarlos
    productos=Producto.objects.all()

    return render(request, 'tienda/tienda.html', {'productos':productos})
