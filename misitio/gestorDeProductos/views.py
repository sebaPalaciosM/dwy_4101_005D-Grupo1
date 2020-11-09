from django.shortcuts import render
from gestorDeProductos.models import Marca, Categoria, Sucursal, Producto
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def plantillaBase(request):
    return render(request, 'plantillaBase.html', {})
    
def registro(request): 
   
    if request.method == "POST":
        nombre    = request.POST["txtNombre"]
        correo    = request.POST["txtCorreo"]
        clave     = request.POST["txtClave"]        
        User.objects.create(username=nombre, email=correo, password=make_password(clave)) 
        
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path)) 
    return render(request, 'registro.html', {})
        
def sucursal(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))    
    mensaje = ""
    lista = {}
    item = {}
    if request.method == "POST":
        id          = int("0" + request.POST["txtId"])
        nombre      = request.POST["txtNombre"]
        direccion   = request.POST["txtDireccion"]
        telefono    = request.POST["txtTelefono"]
        encargado   = request.POST["txtEncargado"]
        
        if 'btnGrabar' in request.POST:
            
            if id < 1:
               Sucursal.objects.create(nombre=nombre, direccion=direccion, telefono=telefono, encargado=encargado)              
               
            else:
                item = Sucursal.objects.get(pk = id)
                item.nombre = nombre
                item.direccion=direccion
                item.telefono=telefono
                item.encargado=encargado
                item.save()
                item = {}
                
            mensaje ="Datos Guardados"
            
        elif 'btnBuscar' in request.POST:
            try:
                item = Sucursal.objects.get(pk = id)
            except:         
                mensaje = "Registro no Encontrado"
                item = {}
                
        elif 'btnListar' in request.POST:
            lista = Sucursal.objects.all()
 
        elif 'btnEliminar' in request.POST:
            item = Sucursal.objects.get(pk = id)
            
            if isinstance(item, Sucursal):
                item.delete()
                mensaje = "Registro Eliminado"
                item = {} 
    contexto = {'mensaje':mensaje, 'lista':lista, 'item':item}    
    return render(request, 'sucursal.html', contexto)    
    
def marca(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))    
    mensaje = ""
    lista = {}
    item = {}
    if request.method == "POST":
        id       = int("0" + request.POST["txtId"])
        nombre   = request.POST["txtNombre"]
        activo   = request.POST.get("chkActivo") is "1"
        
        if 'btnGrabar' in request.POST:
            
            if id < 1:
               Marca.objects.create(nombre = nombre, activo = activo)              
               
            else:
                item = Marca.objects.get(pk = id)
                item.nombre = nombre
                item.activo = activo
                item.save()
                item = {}
                
            mensaje ="Datos Guardados"
            
        elif 'btnBuscar' in request.POST:
            try:
                item = Marca.objects.get(pk = id)
            except:         
                mensaje = "Registro no Encontrado"
                item = {}
                
        elif 'btnListar' in request.POST:
            lista = Marca.objects.all()
 
        elif 'btnEliminar' in request.POST:
            item = Marca.objects.get(pk = id)
            
            if isinstance(item, Marca):
                item.delete()
                mensaje = "Registro Eliminado"
                item = {} 
    contexto = {'mensaje':mensaje, 'lista':lista, 'item':item}    
    return render(request, 'marca.html', contexto)
    
def categoria(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))    
    mensaje = ""
    lista = {}
    item = {}
    if request.method == "POST":
        id       = int("0" + request.POST["txtId"])
        nombre   = request.POST["txtNombre"]
        activo   = request.POST.get("chkActivo") is "1"
        
        if 'btnGrabar' in request.POST:
            
            if id < 1:
               Categoria.objects.create(nombre = nombre, activo = activo)              
               
            else:
                item = Categoria.objects.get(pk = id)
                item.nombre = nombre
                item.activo = activo
                item.save()
                item = {}
                
            mensaje ="Datos Guardados"
            
        elif 'btnBuscar' in request.POST:
            try:
                item = Categoria.objects.get(pk = id)
            except:         
                mensaje = "Registro no Encontrado"
                item = {}
                
        elif 'btnListar' in request.POST:
            lista = Categoria.objects.all()
 
        elif 'btnEliminar' in request.POST:
            item = Categoria.objects.get(pk = id)
            
            if isinstance(item, Categoria):
                item.delete()
                mensaje = "Registro Eliminado"
                item = {} 
    contexto = {'mensaje':mensaje, 'lista':lista, 'item':item}    
    return render(request, 'categoria.html', contexto)
 

def producto(request):
    mensaje = ""
    lista = {}  
    item = {}
    cmbMarca = Marca.objects.all()
    cmbCategoria = Categoria.objects.all()
    
    if request.method == "POST":
        id           = int("0" + request.POST["txtId"])
        idMarca      = int("0" + request.POST["cmbMarca"])
        idCategoria = int("0" + request.POST["cmbCategoria"])
        codigo       = int("0" + request.POST["txtCodigo"])
        descripcion  = request.POST["txtDescripcion"]
        precioCosto  = int("0" + request.POST["txtPrecioCosto"])
        precioVenta  = int("0" + request.POST["txtPrecioVenta"])
        stock        = int("0" + request.POST["txtStock"])
        
        if 'btnGrabar' in request.POST:
            marca = Marca.objects.get(pk = idMarca)
            categoria = Categoria.objects.get(pk = idCategoria)
            if id < 1:                
                Producto.objects.create(marca=marca, categoria=categoria, codigo=codigo, descripcion=descripcion, precioCosto=precioCosto,
                precioVenta=precioVenta, stock=stock)
            else:
                item = Producto.objects.get(pk = id)
                item.marca       = marca
                item.categoria   = categoria
                item.codigo      = codigo
                item.descripcion = descripcion
                item.precioCosto = precioCosto
                item.precioVenta = precioVenta
                item.stock       = stock
                item.save()
                item = {}
            
            
            mensaje = "Los Datos Fueron Guardados"
     
        elif 'btnBuscar' in request.POST:
            try:
                item = Producto.objects.get(pk = id)
            except:         
                mensaje = "Registro no Encontrado"
                item = {}
            
        elif 'btnListar' in request.POST:
            lista = Producto.objects.filter(codigo__contains = codigo, descripcion__contains= descripcion)
        #   lista = Producto.objects.all()
        
        elif 'btnEliminar' in request.POST:
            item = Producto.objects.get(pk = id)
            
            if isinstance(item, Producto):
                item.delete()
                mensaje = "Registro Eliminado"
                item = {}
        

        
    contexto = {'mensaje' : mensaje, 'lista' : lista, 'item' : item, 'cmbMarca' : cmbMarca, 'cmbCategoria' : cmbCategoria}
    return render(request,'producto.html', contexto)
    

    

    
    
    
    
    
    
    