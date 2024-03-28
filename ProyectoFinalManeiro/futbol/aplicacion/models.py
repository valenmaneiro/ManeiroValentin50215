from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Futbolista(models.Model):
    nombreCompleto = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=60)
    equipo = models.CharField(max_length=60)
    dorsal = models.IntegerField()


class Entrenador(models.Model):
    nombreCompleto = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=60)
    equipo = models.CharField(max_length=60)

class Equipo(models.Model):
    nombre = models.CharField(max_length=60)
    pais = models.CharField(max_length=60)
    nroSocios = models.IntegerField()
    fechaFundacion = models.DateField()

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
    
class Representante(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    agencia = models.CharField(max_length=60)
    email = models.EmailField()