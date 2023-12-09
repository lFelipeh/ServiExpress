from django import forms
from .models import Cliente, Reserva, Boleta, Proveedor, Empleado, Servicio, OrdenPedido, RecepcionProducto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'direccion']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'servicio', 'fecha_hora', 'notas']
        widgets = {
            'fecha_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class FormularioRegistroUsuario(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FormularioBoleta(forms.ModelForm):
    class Meta:
        model = Boleta
        fields = ['cliente', 'total']

class FormularioProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre_empresa', 'contacto_nombre', 'contacto_email']

class FormularioEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'posicion', 'email']

class FormularioServicio(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'costo']


class FormularioOrdenPedido(forms.ModelForm):
    class Meta:
        model = OrdenPedido
        fields = ['proveedor', 'entregado']

class FormularioRecepcionProducto(forms.ModelForm):
    class Meta:
        model = RecepcionProducto
        fields = ['orden_pedido', 'fecha_recepcion', 'cantidad_recibida', 'notas']
