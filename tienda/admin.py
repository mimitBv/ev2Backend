from django.contrib import admin
from .models import (

Cliente,
Categoria, 
MetodoPago, 
Sucursal, 
Producto, 
Inventario, 
Franquicia, 
Pedido, 
Empleado 
)
# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'correo', 'telefono', 'direccion')
    search_fields = ('rut', 'nombre', 'correo', 'telefono')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    search_fields = ('nombre', 'direccion', 'telefono')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):  
    list_display = ('sku', 'nombre', 'marca', 'precio', 'categoria')
    search_fields = ('sku', 'nombre', 'marca', 'categoria__nombre')
    list_filter = ('categoria',)    

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'sucursal', 'cantidad')
    search_fields = ('producto__nombre', 'sucursal__nombre')
    list_filter = ('sucursal',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):    
    list_display = ('id_pedido', 'cliente', 'fecha', 'total', 'metodo_pago')
    search_fields = ('id_pedido', 'cliente__nombre', 'cliente__rut', 'metodo_pago__nombre')
    list_filter = ('fecha', 'metodo_pago')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id_empleado', 'nombre', 'correo',  'sucursal')
    search_fields = ('nombre', 'correo', 'sucursal')
    list_filter = ('sucursal',)

@admin.register(Franquicia)
class FranquiciaAdmin(admin.ModelAdmin):
    list_display = ('id_franquicia', 'nombre', 'direccion')
    search_fields = ('nombre', 'direccion', 'sucursal__nombre')
