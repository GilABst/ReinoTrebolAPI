from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Afinidad_Magicas(models.Model):
    afinidadMagica = models.CharField(max_length=20)

    def __str__(self):
       return self.afinidadMagica

class Grimorios(models.Model):
    categoria = models.CharField(max_length=20)
    trebol = models.PositiveIntegerField(validators=[MaxValueValidator(5)])

class Aspirante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    identificacion = models.CharField(max_length=10)
    edad = models.PositiveIntegerField(validators=[MaxValueValidator(99)])
    afinidadMagica = models.ForeignKey(Afinidad_Magicas, on_delete = models.CASCADE)
    grimorio = models.ForeignKey(Grimorios, on_delete = models.CASCADE, null=True)
    status = models.BooleanField(default=False)