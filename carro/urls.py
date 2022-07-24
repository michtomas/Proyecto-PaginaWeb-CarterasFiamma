from django.urls import path
from . import views

app_name='carro'

urlpatterns = [
    path("agregar/<int:id>/", views.agregar_producto, name='agregar'),
    path("eliminar/<int:id>/", views.eliminar_producto, name='eliminar'),
    path('vaciar/', views.vaciar_carrito, name='vaciar')
    ]
