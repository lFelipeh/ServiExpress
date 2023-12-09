from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    contacto_nombre = models.CharField(max_length=100)
    contacto_email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre_empresa

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True)
    fecha_hora = models.DateTimeField()
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"{self.cliente.nombre} - {self.servicio.nombre} en {self.fecha_hora}"

class Boleta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_emision = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Boleta {self.id} - {self.cliente.nombre}"

class OrdenPedido(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return f"Orden de Pedido {self.id} - {self.proveedor.nombre_empresa}"

class RecepcionProducto(models.Model):
    orden_pedido = models.ForeignKey(OrdenPedido, on_delete=models.CASCADE)
    fecha_recepcion = models.DateField()
    cantidad_recibida = models.IntegerField()
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Recepción para {self.orden_pedido} en {self.fecha_recepcion}"