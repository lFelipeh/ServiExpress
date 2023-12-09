from django.contrib import admin
from .models import Cliente, Servicio, Empleado, Proveedor, Reserva

admin.site.register(Cliente)
admin.site.register(Servicio)
admin.site.register(Empleado)
admin.site.register(Proveedor)
admin.site.register(Reserva)
