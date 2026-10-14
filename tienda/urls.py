

from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    
    # Lista de todas tus páginas estáticas
    path('acceso_restringido.html', TemplateView.as_view(template_name='acceso_restringido.html'), name='acceso_restringido'),
    path('carrito.html', TemplateView.as_view(template_name='carrito.html'), name='carrito'),
    path('catalogo_espanol.html', TemplateView.as_view(template_name='catalogo_espanol.html'), name='catalogo_espanol'),
    path('catalogo.html', TemplateView.as_view(template_name='catalogo.html'), name='catalogo'),
    path('compra.html', TemplateView.as_view(template_name='compra.html'), name='compra'),
    path('detalle_producto_carrito_alternativo.html', TemplateView.as_view(template_name='detalle_producto_carrito_alternativo.html'), name='detalle_producto_carrito_alt'),
    path('detalle_producto_carrito.html', TemplateView.as_view(template_name='detalle_producto_carrito.html'), name='detalle_producto_carrito'),
    path('iniciar_sesion_cliente.html', TemplateView.as_view(template_name='iniciar_sesion_cliente.html'), name='iniciar_sesion_cliente'),
    path('iniciar_sesion.html', TemplateView.as_view(template_name='iniciar_sesion.html'), name='iniciar_sesion'),
    path('panel_administracion.html', TemplateView.as_view(template_name='panel_administracion.html'), name='panel_administracion'),
    path('panel_bodega.html', TemplateView.as_view(template_name='panel_bodega.html'), name='panel_bodega'),
    path('portal_cliente.html', TemplateView.as_view(template_name='portal_cliente.html'), name='portal_cliente'),
    path('registro.html', TemplateView.as_view(template_name='registro.html'), name='registro'),
    path('seguimiento_pedido.html', TemplateView.as_view(template_name='seguimiento_pedido.html'), name='seguimiento_pedido'),
    path('sucursales_franquicias.html', TemplateView.as_view(template_name='sucursales_franquicias.html'), name='sucursales_franquicias'),
    path('sucursales.html', TemplateView.as_view(template_name='sucursales.html'), name='sucursales'),
    path('tienda.html', TemplateView.as_view(template_name='tienda.html'), name='tienda'),
]
