# Generated by Django 3.1.2 on 2020-11-09 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorDeProductos', '0004_auto_20201108_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=50)),
                ('direccion', models.TextField(max_length=200)),
                ('telefono', models.TextField(max_length=9)),
                ('encargado', models.TextField(max_length=100)),
            ],
        ),
    ]
