from django import forms

from pedidos.models import Pedido

class formularioPedido(forms.ModelForm):
    class Meta:
        model = Pedido    
        fields = '__all__'
        