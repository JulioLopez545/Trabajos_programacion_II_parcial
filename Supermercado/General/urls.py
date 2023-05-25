from django.urls import path
from .views import *

urlpatterns = [
    path('cargos/', ObtenerCargos.as_view(), name='listar_cargos'),
    path('cargos/agregar', AgregarCargo.as_view(), name='agregar_cargos'),
    path('cargos/<uuid:uuid>/Actualizar', ActualizarCargo.as_view(), name='actualizar_cargos'),
    path('clientes/<uuid:uuid>/Actualizar', ActualizarClientes.as_view(), name='actualizar_clientes'),
    path('clientes/', ObtenerClientes.as_view(), name='listar_clientes'),
    path('clientes/agregar', AgregarClientes.as_view(), name='agregar_cliente'),
    path('usuarios/', ObtenerUsuarios.as_view(), name='listar_usuarios'),
    path('usuarios/agregar', AgregarUsuarios.as_view(), name='agregar_usuarios'),
    path('usuarios/<uuid:uuid>/Actualizar', ActualizarUsuarios.as_view(), name='actualizar_usuarios'),
]