from django.contrib import admin
from .models import Marca, Categoria, Sucursal, Producto
# Register your models here.
class marcaAdmin(admin.ModelAdmin):
    list_display        = ['nombre','activo' ]
    list_display_links  = ['nombre','activo' ]
    list_filter         = ['nombre']
    search_fields       = ['nombre']

class categoriaAdmin(admin.ModelAdmin):
    list_display        = ['nombre','activo' ]
    list_display_links  = ['nombre','activo' ]
    list_filter         = ['nombre']
    search_fields       = ['nombre']

class sucursalAdmin(admin.ModelAdmin):
    list_display        = ['nombre','direccion','telefono','encargado']
    list_display_links  = ['nombre','encargado']
    list_filter         = ['nombre','encargado']
    search_fields       = ['nombre','encargado']

class productoAdmin(admin.ModelAdmin):
    list_display        = ['marca','categoria','codigo','descripcion', 'stock', 'precioCosto', 'precioVenta']
    list_display_links  = ['marca','categoria']
    list_filter         = ['codigo','categoria','marca']
    search_fields       = ['codigo','categoria','marca']
    
admin.site.register(Marca, marcaAdmin)
admin.site.register(Categoria, categoriaAdmin)
admin.site.register(Sucursal, sucursalAdmin)
admin.site.register(Producto, productoAdmin)