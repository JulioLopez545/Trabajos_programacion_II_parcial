from django.urls import path
from .views import *

urlpatterns = [
    path('proveedores/', ListarProveedores.as_view(), name='listar_proveedores'),
    path('proveedores/agregar', AgregarProveedor.as_view(), name='agregar_proveedor'),
    path('proveedores/<uuid:uuid>/profile', ObtenerProveedorPorUUID.as_view(), name='obtener_proveedor_por_uuid'),
    path('proveedores/<uuid:uuid>/actualizar', ActualizarProveedor.as_view(), name='actualizar_proveedor'),
    path('productos/', ListarProductos.as_view(), name='listar_productos'),
    path('productos//<uuid:uuid>/actualizar', ActualizarProductos.as_view(), name='actualizar_productos'),
    path('productos/Add', AgregarProducto.as_view(), name='agregar_productos'),
    path('productos/<uuid:uuid>/profile', ObtenerProductoPorUUID.as_view(), name='obtener_producto_por_uuid'),
]