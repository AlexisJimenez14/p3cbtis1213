from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("contactos/",views.contactos,name="contactos"),
    path("empleado/",views.empleado,name="empleado"),
    path("cliente/",views.cliente,name="cliente"),
    path("envios/",views.envios,name="envios"),
    path("proveedores/",views.proveedores,name="proveedores"),
    
]
