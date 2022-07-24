from django.urls import path
from .views import Registro
from .views import cerrar_sesion, loggear

urlpatterns = [
    path('', Registro.as_view(), name='Autentificacion'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
    path('loggear', loggear, name='loggear'),
    ]