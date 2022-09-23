from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre=models.CharField(max_length=60)
    
    duracion=models.IntegerField()

class Profesor(models.Model):

    nombre=models.CharField(max_length=60)

    email=models.EmailField()

class Ubicacion(models.Model):

    nombre=models.CharField(max_length=60)

    cantAlumnos=models.IntegerField()


