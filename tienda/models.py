from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError






class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class MetodoPago(models.Model):
    METODOS_PERMITIDOS = [
        ('transbank', 'Webpay / Transbank (Débito-Crédito)'),
        ('cuenta_rut', 'Transferencia BancoEstado (Cuenta RUT)'),
        ('efectivo', 'Pago en Efectivo (Solo Retiro)'),
        ('paypal', 'PayPal (Dólares)'),
        ('mercado_pago', 'Mercado Pago (Dólares o Pesos)'),
        ('otro', 'Otro Método de Pago')
    ]

    id_metodo_pago = models.AutoField(primary_key=True)
    
    nombre = models.CharField(
        max_length=50,
        choices=METODOS_PERMITIDOS,
        default='transbank',
        unique=True 
    )

    def __str__(self):
        
        return self.get_nombre_display()


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=50, unique=True, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField()
    precio = models.IntegerField()  
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return f"{self.marca} - {self.nombre}" if self.marca else self.nombre


class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=12, blank=True, null=True, help_text="Formato: +569XXXXXXXX")

    def __str__(self):
        return self.nombre


class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='inventarios')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='inventarios')
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.producto.nombre} en {self.sucursal.nombre} ({self.cantidad} un.)"


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    
    
    rut = models.CharField(max_length=12,unique=True,)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=12, blank=True, null=True, help_text="Formato: +569XXXXXXXX")
    direccion = models.TextField()

    def __str__(self):
        return f"{self.rut} - {self.nombre}"


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente de Pago'),
        ('pagado', 'Pagado / Preparando'),
        ('enviado', 'Enviado a Despacho'),
        ('entregado', 'Entregado'),
    ]
    
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='pedidos')
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.PROTECT, related_name='pedidos')
    total = models.IntegerField(default=0)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"Pedido N° {self.id} - {self.cliente.nombre}"


class DetallePedido(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, related_name='detalles_pedido')
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.IntegerField()

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad} (Pedido N° {self.pedido.id})"


class Franquicia(models.Model):
    id_franquicia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='franquicias')
   

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    cargo = models.CharField(max_length=50)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='empleados')
    sueldo = models.IntegerField()



    def __str__(self):
        return self.nombre
