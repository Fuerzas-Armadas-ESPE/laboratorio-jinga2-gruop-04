from django.shortcuts import render
from .models import Producto

productos = []

def listar_productos(request):
<<<<<<< HEAD
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})
=======
    # Consulta a la base de datos
    # Renderiza la plantilla listar.html
>>>>>>> 19ce850d91ef4927ab7c10f0b0386b476dc2c901
