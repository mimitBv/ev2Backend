from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def iniciar_sesion(request):
    return render(request, 'iniciar_sesion.html')

def panel_admin(request):
    return render(request, 'panel_admin.html')

def acceso_restringido(request):
    return render(request, 'acceso_restringido.html')

def carrito(request):
    return render(request, 'carrito.html')

def catalogo(request):
    return render(request, 'catalogo.html')

def catalogo_espanol(request):
    return render(request, 'catalogo_espanol.html')

def compra(request):
    return render(request, 'compra.html')

def detalle_producto_carrito(request):
    return render(request, 'detalle_producto_carrito.html')

def detalle_producto_carrito_alternativo(request):
    return render(request, 'detalle_producto_carrito_alternativo.html')

def iniciar_sesion_cliente(request):
    return render(request, 'iniciar_sesion_cliente.html')

def panel_bodega(request):
    return render(request, 'panel_bodega.html')

def portal_cliente(request):
    return render(request, 'portal_cliente.html')

def registro(request):
    return render(request, 'registro.html')

def seguimiento_pedido(request):
    return render(request, 'seguimiento_pedido.html')

def sucursales_franquicias(request):
    return render(request, 'sucursales_franquicias.html')

def sucursales(request):
    return render(request, 'sucursales.html')

def tienda(request):
    return render(request, 'tienda.html')