
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='rut',
            field=models.CharField(
                max_length=12,
                null=True,
                blank=True,
            ),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(
                max_length=12,
                help_text='Formato: +569XXXXXXXX',
            ),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rut',
            field=models.CharField(
                max_length=12,
                unique=True,
            ),
        ),
    ]

