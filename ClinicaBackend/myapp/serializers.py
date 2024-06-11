from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import Contacto,Medico,Paciente,Reserva

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields ="__all__"

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields ="__all__"

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields ="__all__"

class ReservaSerializer(serializers.ModelSerializer):
    paciente_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Reserva
        fields = ['id_reserva', 'fecha', 'hora', 'paciente', 'paciente_nombre', 'medico']

    def get_paciente_nombre(self, obj):
        return f"{obj.paciente.nombrepa} ({obj.paciente.rut_paciente})"