from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contactos(request):
    return render(request, 'contactos.html')

def empleado(request):
    return render(request, 'empleado.html')

def cliente(request):
    return render(request, 'cliente.html')

def envios(request):
    return render(request, 'envios.html')

def proveedores(request):
    return render(request, 'proveedores.html')

