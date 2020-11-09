from django.urls import path
from . import views

urlpatterns = [ 
    path('plantillaBase', views.plantillaBase, name='plantillaBase'),
    path('marca', views.marca, name='marca'),
    path('registro', views.registro, name='registro'),
    path('categoria', views.categoria, name='categoria'),
    path('sucursal', views.sucursal, name='sucursal'),
    path('producto', views.producto, name='producto'),

]

