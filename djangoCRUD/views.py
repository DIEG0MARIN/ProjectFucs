from django.shortcuts import render, redirect
from.models import Prestamos
from django.utils import timezone
# Create your views here.

def home(request):
    prestamos = Prestamos.objects.all()
    return render(request, 'index.html', {'Prestamos': prestamos})


def agregar(request):
    if request.method == 'POST':
        try:
            nombres = request.POST.get('nombre') + ' ' + request.POST.get('apellido')
            telefono = int(request.POST.get('telefono'))
            correo = request.POST.get('correo')
            facultad = request.POST.get('facultad')
            fecha = timezone.now()

            Prestamos.objects.create(
                nombres=nombres,
                telefono=telefono,
                correo=correo,
                facultad=facultad,
                fecha=fecha
            )
            return redirect('home')
        except Exception as e:
            # Manejar la excepción adecuadamente
            print(f"Error al agregar registro: {e}")

    return render(request, 'index.html')