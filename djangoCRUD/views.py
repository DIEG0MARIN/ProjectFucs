from django.shortcuts import render
from.models import Prestamos

# Create your views here.

def home(request):
    prestamos = Prestamos.objects.all()
    return render(request, 'index.html', {'Prestamos': prestamos})