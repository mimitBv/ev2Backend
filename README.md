# MusicPro - Evaluación 2

Aplicación web desarrollada con Django para la gestión de la tienda de instrumentos musicales MusicPro. Incluye catálogo de productos, carrito de compras, sucursales y paneles de administración y bodega.

## Requisitos

- Python 3.14
- `pip`

## Instalación y ejecución

Desde la carpeta del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Configura una clave de Django para el entorno local. Puedes generar una con:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copia el valor generado y expórtalo antes de iniciar la aplicación:

```bash
export DJANGO_SECRET_KEY="pega-aqui-la-clave-generada"
```

Luego prepara la base de datos e inicia el servidor:

```bash
python manage.py migrate
python manage.py runserver
```

La aplicación estará disponible en `http://127.0.0.1:8000/`. Para acceder al panel de administración en `/admin/`, crea un superusuario:

```bash
python manage.py createsuperuser
```

La base de datos SQLite y la clave secreta local no se incluyen en el repositorio. Define `DJANGO_SECRET_KEY` también en cualquier entorno desplegado; el valor de desarrollo predeterminado de la configuración no es seguro para producción.
