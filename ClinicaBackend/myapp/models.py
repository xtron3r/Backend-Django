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
    rut = models.CharField(max_length=11, primary_key=True, unique=True)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f" {self.rut} - {self.nombrem} - {self.especialidad}"
    
class Paciente(models.Model):
    nombreCompleto = models.CharField(max_length=80)
    rut= models.CharField(max_length=11, primary_key=True, unique=True )
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)
    prevision = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.nombreCompleto} - {self.rut} - {self.especialidad} - {self.medico} - {self.prevision} "
class Horas(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    prevision_paciente = models.CharField(max_length=60)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField() 

    def __str__(self):
        return f"{self.paciente} - {self.prevision_paciente} - {self.especialidad} - {self.medico} - {self.fecha} - {self.hora} "
    




    
