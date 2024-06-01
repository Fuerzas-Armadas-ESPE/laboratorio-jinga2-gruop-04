from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('productos.urls'))
=======
    # Crear la URL de la app productos
>>>>>>> 19ce850d91ef4927ab7c10f0b0386b476dc2c901
]