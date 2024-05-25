from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombrec = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.nombrec} - {self.motivo}"

class Medico(models.Model):
    nombrem = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    
