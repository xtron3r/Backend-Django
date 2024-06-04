from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombrec = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=300)

    def __str__(self):
        return f"NOMBRE COMPLETO: {self.nombrec} | MOTIVO: {self.motivo} | EMAIL: {self.email} | TELEFONO: {self.telefono} | MENSAJE: {self.mensaje}"

class Medico(models.Model):
    nombrem = models.CharField(max_length=100)
    rut = models.CharField(max_length=11, primary_key=True, unique=True)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f"NOMBRE MEDICO: {self.nombrem} | RUT: {self.rut} | ESPECIALIDAD: {self.especialidad}"
    
class Paciente(models.Model):
    PREVIS = [
        ('FONASA','Fonasa'),
        ('ISAPRE','Isapre'),
        ('PARTICULAR','Particular'),
    ]
    nombreCompleto = models.CharField(max_length=80)
    rut= models.CharField(max_length=11, primary_key=True, unique=True )
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    prevision = models.CharField(max_length=20, choices=PREVIS)

    def __str__(self):
        return f"NOMBRE PACIENTE: {self.nombreCompleto} | RUT: {self.rut} | PREVISION: {self.prevision} "
class Horas(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField() 

    def __str__(self):
        return f"{self.paciente} | {self.medico} | FECHA AGENDADA: {self.fecha} / {self.hora} HRS "
    




    
