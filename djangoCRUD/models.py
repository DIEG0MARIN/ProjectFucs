from django.db import models

# Create your models here.

class Prestamos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=30)
    perfil = models.CharField(max_length=30)
    telefono = models.IntegerField()  # Cambiado de CharField a IntegerField
    correo = models.CharField(max_length=50)
    facultad = models.CharField(max_length=40)
    numeroPortatil = models.IntegerField()
    fecha = models.IntegerField()
    observaciones = models.CharField(max_length=100)

    def __str__(self): 
        text = "{0} {1}"
        return text.format(self.id ,self.nombres)
