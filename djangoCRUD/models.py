from django.db import models

# Create your models here.
class Prestamos(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length = 30)
    perfil = models.CharField(max_length = 30)
    telefono = models.CharField(max_length = 20)
    correo = models.CharField(max_length = 50)
    facultad = models.CharField(max_length = 40)
    numeroPortatil = models.CharField(max_length = 10)
    fecha = models.CharField(max_length = 40)
    observaciones = models.CharField(max_length = 100)