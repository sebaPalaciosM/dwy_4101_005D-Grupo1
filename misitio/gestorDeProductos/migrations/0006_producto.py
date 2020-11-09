# Generated by Django 3.1.2 on 2020-11-09 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestorDeProductos', '0005_sucursal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.DecimalField(decimal_places=0, max_digits=13)),
                ('descripcion', models.TextField(max_length=150)),
                ('stock', models.IntegerField()),
                ('precioCosto', models.IntegerField()),
                ('precioVenta', models.IntegerField()),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorDeProductos.categoria')),
                ('marca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorDeProductos.marca')),
            ],
        ),
    ]