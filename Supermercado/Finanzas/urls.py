from django.urls import path
from .views import *

urlpatterns = [ 
    path('facturas/', ObtenerFacturas.as_view(),name='listar_facturas'),
    path('facturas/agregar', AgregarFacturas.as_view(), name='agregar_facturas'),
    path('facturas/<uuid:uuid>/Actualizar', ActualizarFacturas.as_view(), name='actualizar_facturas'),
]