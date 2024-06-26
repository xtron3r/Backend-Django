from django.db import models
import uuid

# Create your models here.

class Contacto(models.Model):
    nombrec = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=300)

    def __str__(self):
        return f"NOMBRE COMPLETO: {self.nombrec} | MOTIVO: {self.motivo} | EMAIL: {self.email} | TELEFONO: {self.telefono} | MENSAJE: {self.mensaje}"

class Paciente(models.Model):
    PREVIS = [
        ('FONASA','Fonasa'),
        ('ISAPRE','Isapre'),
        ('PARTICULAR','Particular'),
    ]
    nombrepa = models.CharField(max_length=80)
    rut_paciente = models.CharField(max_length=11, primary_key=True, unique=True)
    prevision = models.CharField(max_length=20, choices=PREVIS)

    def __str__(self):
        return f"NOMBRE PACIENTE: {self.nombrepa} | RUT: {self.rut_paciente} | PREVISION: {self.prevision}"

class Medico(models.Model):
    nombrem = models.CharField(max_length=100)
    rut_medico = models.CharField(max_length=11, primary_key=True, unique=True)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f"NOMBRE MEDICO: {self.nombrem} | RUT: {self.rut_medico} | ESPECIALIDAD: {self.especialidad}"
    
class Reserva(models.Model):
    id_reserva = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # DA UN ID ALEATORIO
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"ID RESERVA: {self.id_reserva} | PACIENTE: {self.paciente.nombrepa} | RUT PACIENTE: {self.paciente.rut_paciente} | PREVISION: {self.paciente.prevision} | MEDICO: {self.medico.nombrem} | RUT MEDICO: {self.medico.rut_medico} | ESPECIALIDAD MEDICO: {self.medico.especialidad} | FECHA Y HORA: {self.fecha} {self.hora}"


