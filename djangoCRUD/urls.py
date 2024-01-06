
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('agregar/', views.agregar, name='agregar'),
    # path('agregar/', views.agregar)
    
]
