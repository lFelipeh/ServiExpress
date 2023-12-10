from django.shortcuts import render, redirect
from .models import Cliente, Reserva, Proveedor,Empleado, Servicio, Boleta, OrdenPedido, RecepcionProducto
from .forms import ClienteForm, ReservaForm, FormularioRegistroUsuario, FormularioProveedor, FormularioEmpleado, FormularioServicio, FormularioBoleta, FormularioOrdenPedido , FormularioRecepcionProducto
from django.contrib.auth import authenticate, login
from django.db.models import Count, Sum
from django.contrib.auth.decorators import login_required

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestion_clientes/lista_clientes.html', {'clientes': clientes})

@login_required
def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'gestion_clientes/form_cliente.html', {'form': form})

@login_required
def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'gestion_clientes/lista_reservas.html', {'reservas': reservas})

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm()
    return render(request, 'gestion_clientes/form_reserva.html', {'form': form})

@login_required
def editar_reserva(request, id):
    reserva = Reserva.objects.get(id=id)
    form = ReservaForm(request.POST or None, instance=reserva)
    if form.is_valid():
        form.save()
        return redirect('lista_reservas')
    return render(request, 'gestion_clientes/form_reserva.html', {'form': form, 'reserva': reserva})

@login_required
def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'gestion_clientes/form_cliente.html', {'form': form})

@login_required
def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('lista_clientes')


def registrar(request):
    if request.method == 'POST':
        formulario = FormularioRegistroUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            nombre_usuario = formulario.cleaned_data.get('username')
            contraseña = formulario.cleaned_data.get('password1')
            usuario = authenticate(username=nombre_usuario, password=contraseña)
            login(request, usuario)
            return redirect('acceder')
    else:
        formulario = FormularioRegistroUsuario()
    return render(request, 'gestion_clientes/registrar.html', {'formulario': formulario})

def acceder(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_clientes')  # Cambia a la URL deseada después del login
        else:
            return render(request, 'gestion_clientes/acceder.html', {'error': 'Credenciales incorrectas'})
    else:
        return render(request, 'gestion_clientes/acceder.html')

@login_required
def lista_boletas(request):
    boletas = Boleta.objects.all()
    return render(request, 'gestion_clientes/lista_boletas.html', {'boletas': boletas})

@login_required
def crear_boleta(request):
    if request.method == 'POST':
        form = FormularioBoleta(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_boletas')
    else:
        form = FormularioBoleta()
    return render(request, 'gestion_clientes/form_boleta.html', {'form': form})

@login_required
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'gestion_clientes/lista_proveedores.html', {'proveedores': proveedores})

@login_required
def crear_proveedor(request):
    if request.method == 'POST':
        form = FormularioProveedor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = FormularioProveedor()
    return render(request, 'gestion_clientes/form_proveedor.html', {'form': form})

@login_required
def editar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    if request.method == 'POST':
        form = FormularioProveedor(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = FormularioProveedor(instance=proveedor)
    return render(request, 'gestion_clientes/form_proveedor.html', {'form': form})

@login_required
def eliminar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    return redirect('lista_proveedores')

@login_required
def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'gestion_clientes/lista_empleados.html', {'empleados': empleados})

@login_required
def crear_empleado(request):
    if request.method == 'POST':
        form = FormularioEmpleado(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = FormularioEmpleado()
    return render(request, 'gestion_clientes/form_empleado.html', {'form': form})

@login_required
def editar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    if request.method == 'POST':
        form = FormularioEmpleado(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = FormularioEmpleado(instance=empleado)
    return render(request, 'gestion_clientes/form_empleado.html', {'form': form})

@login_required
def eliminar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('lista_empleados')

@login_required
def lista_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'gestion_clientes/lista_servicios.html', {'servicios': servicios})

@login_required
def crear_servicio(request):
    if request.method == 'POST':
        form = FormularioServicio(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_servicios')
    else:
        form = FormularioServicio()
    return render(request, 'gestion_clientes/form_servicio.html', {'form': form})

@login_required
def editar_servicio(request, id):
    servicio = Servicio.objects.get(id=id)
    if request.method == 'POST':
        form = FormularioServicio(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('lista_servicios')
    else:
        form = FormularioServicio(instance=servicio)
    return render(request, 'gestion_clientes/form_servicio.html', {'form': form})

@login_required
def eliminar_servicio(request, id):
    servicio = Servicio.objects.get(id=id)
    servicio.delete()
    return redirect('lista_servicios')

@login_required
def lista_ordenes_pedido(request):
    ordenes = OrdenPedido.objects.all()
    return render(request, 'gestion_clientes/lista_ordenes_pedido.html', {'ordenes': ordenes})

@login_required
def crear_orden_pedido(request):
    if request.method == 'POST':
        form = FormularioOrdenPedido(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ordenes_pedido')
    else:
        form = FormularioOrdenPedido()
    return render(request, 'gestion_clientes/form_orden_pedido.html', {'form': form})


@login_required
def lista_recepciones(request):
    recepciones = RecepcionProducto.objects.all()
    return render(request, 'gestion_clientes/lista_recepciones.html', {'recepciones': recepciones})

@login_required
def crear_recepcion(request):
    if request.method == 'POST':
        form = FormularioRecepcionProducto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_recepciones')
    else:
        form = FormularioRecepcionProducto()
    return render(request, 'gestion_clientes/form_recepcion.html', {'form': form})

@login_required
def informes(request):
    num_clientes = Cliente.objects.count()
    num_reservas = Reserva.objects.count()
    ingresos_totales = Boleta.objects.aggregate(Sum('total'))

    return render(request, 'gestion_clientes/informes.html', {
        'num_clientes': num_clientes,
        'num_reservas': num_reservas,
        'ingresos_totales': ingresos_totales['total__sum']
    })

@login_required
def eliminar_orden_pedido(request, id):
    orden = get_object_or_404(OrdenPedido, id=id)
    if request.method == 'POST':
        orden.delete()
        return redirect('lista_ordenes_pedido')
    return render(request, 'gestion_clientes/confirmar_eliminacion.html', {'orden': orden})
