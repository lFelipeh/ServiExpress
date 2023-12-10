"""
URL configuration for serviexpress project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestion_clientes import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.acceder, name='home'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('reservas/crear/', views.crear_reserva, name='crear_reserva'),
    path('reservas/editar/<int:id>/', views.editar_reserva, name='editar_reserva'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('registro/', views.registrar, name='registrar'),
    path('acceso/', views.acceder, name='acceder'),
    path('boletas/', views.lista_boletas, name='lista_boletas'),
    path('boletas/crear/', views.crear_boleta, name='crear_boleta'),
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('proveedores/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:id>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('empleados/crear/', views.crear_empleado, name='crear_empleado'),
    path('empleados/editar/<int:id>/', views.editar_empleado, name='editar_empleado'),
    path('empleados/eliminar/<int:id>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('servicios/', views.lista_servicios, name='lista_servicios'),
    path('servicios/crear/', views.crear_servicio, name='crear_servicio'),
    path('servicios/editar/<int:id>/', views.editar_servicio, name='editar_servicio'),
    path('servicios/eliminar/<int:id>/', views.eliminar_servicio, name='eliminar_servicio'),
    path('ordenes_pedido/', views.lista_ordenes_pedido, name='lista_ordenes_pedido'),
    path('ordenes_pedido/editar/<int:id>/', views.crear_orden_pedido, name='crear_orden_pedido'),
    path('ordenes_pedido/crear/', views.crear_orden_pedido, name='crear_orden_pedido'),
    path('recepciones/', views.lista_recepciones, name='lista_recepciones'),
    path('recepciones/crear/', views.crear_recepcion, name='crear_recepcion'),
    path('informes/', views.informes, name='informes'),
    path('ordenes_pedido/eliminar/<int:id>/', views.eliminar_orden_pedido, name='eliminar_orden_pedido'),
]