#aca va la variable global del total de la compra
import re
from .carro import Carro

def importe_total(request):
    carro=Carro(request)
    total=0
    #si el usuario esta autenticado entonces que empiece a sumar
    if request.user.is_authenticated:
        for key, value in request.session['carro'].items():
            total+=(float(value['precio']))
    return {'importe_total':total}
