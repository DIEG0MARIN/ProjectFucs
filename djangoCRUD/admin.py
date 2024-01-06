from django.contrib import admin
from .models import Prestamos

# Register your models here.
# admin.site.register(Prestamos)
from django import forms
from django.contrib import admin
from .models import Prestamos

class PrestamosForm(forms.ModelForm):
    class Meta:
        model = Prestamos
        fields = '__all__'

class PrestamosAdmin(admin.ModelAdmin):
    
    list_display = ['identificacion', 'nombres', 'apellidos', 'telefono', 'correo', 'perfil', 'facultad', 'fecha', 'portatil']
    search_fields = ['identificacion', 'nombres', 'apellidos', 'correo']

admin.site.register(Prestamos, PrestamosAdmin)