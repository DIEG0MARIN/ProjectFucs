from django.db import models

# Create your models here.


class Prestamos(models.Model):
    identificacion = models.CharField(primary_key=True, max_length=15)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15, blank=True)
    correo = models.EmailField(max_length=50)
    perfil = models.CharField(max_length=30)
    facultad = models.CharField(max_length=40, blank=True)
    fecha = models.DateTimeField(auto_now_add=True) 
    portatil = models.CharField(max_length=15, blank=True)

    def __str__(self): 
        return f"{self.identificacion} - {self.nombres} {self.apellidos}"


    def __str__(self): 
        text = "{0} {1}"
        return text.format(self.id ,self.nombres, self.apellidos)
