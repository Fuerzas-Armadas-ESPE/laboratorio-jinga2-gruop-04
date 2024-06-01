from django.db import models

<<<<<<< HEAD
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre
=======
# Create your models here.
>>>>>>> 19ce850d91ef4927ab7c10f0b0386b476dc2c901
