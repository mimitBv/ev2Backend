from django.core.management.base import BaseCommand
from tienda.models import Cliente, Categoria, MetodoPago, Sucursal, Producto
from faker import Faker
import random

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        
        
        fake = Faker('es_CL') 
        self.stdout.write("Generando clientes de prueba...")


        for _ in range(100):
            Cliente.objects.create(
            rut=str(fake.unique.random_int(min=10000000, max=25000000)),
            nombre=fake.name(),
            correo=fake.unique.email(),
            telefono=fake.numerify(text="+569########"), 
            direccion=fake.address()
        )

        self.stdout.write('Poblando Categorías...')
        cat1 = Categoria.objects.create(nombre='Guitarras y Bajos')
        cat2 = Categoria.objects.create(nombre='Teclados y Pianos')
        cat3 = Categoria.objects.create(nombre='Baterías y Percusión')
        cat4 = Categoria.objects.create(nombre='Audio Profesional')
        cat5 = Categoria.objects.create(nombre='Accesorios y Otros')

        categorias = [cat1, cat2, cat3, cat4, cat5]

        self.stdout.write('Poblando Sucursales...')
        suc1 = Sucursal.objects.create(nombre='Sucursal Santiago Centro', direccion='Av. Libertador Bernardo O\'Higgins 1234, Santiago, Chile')
        suc2 = Sucursal.objects.create(nombre='Sucursal Providencia', direccion='Av. Providencia 5678, Providencia, Chile')
        suc3 = Sucursal.objects.create(nombre='Sucursal Las Condes', direccion='Av.Las Condes 9101, Las Condes, Chile')         

        sucursales = [suc1, suc2, suc3]


        self.stdout.write('Poblando Métodos de Pago...')
        mp1 = MetodoPago.objects.create(nombre='Tarjeta de Crédito')
        mp2 = MetodoPago.objects.create(nombre='Tarjeta de Débito')
        mp3 = MetodoPago.objects.create(nombre='Transferencia Bancaria')
        mp4 = MetodoPago.objects.create(nombre='Efectivo')
        mp5 = MetodoPago.objects.create(nombre='PayPal')
        mp6 = MetodoPago.objects.create(nombre='Mercado Pago')

        self.stdout.write('Poblando Solicitudes de franquicia...')
        for _ in range(20):
            producto = Producto.objects.create(
                sku=fake.unique.bothify(text='???-#####'),
                nombre=fake.word().capitalize(),
                marca=fake.company(),
                descripcion=fake.text(max_nb_chars=200),
                precio=random.randint(10_000, 1_000_000),
                categoria=random.choice(categorias)
            )
            
            sucursal = random.choice(sucursales)
            sucursal.inventarios.create(producto=producto, cantidad=random.randint(1, 50))

    


        self.stdout.write(self.style.SUCCESS('¡Se crearon los datos con Faker con éxito! 🎉'))

    