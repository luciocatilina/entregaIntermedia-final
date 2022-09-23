from django.urls import path
from .views import *

urlpatterns = [
    path('cursos', cursos, name='curso'),
    path('ubicacion', ubicacion, name='ubicacion'),
    path('buscar', buscar, name='buscar')
]
