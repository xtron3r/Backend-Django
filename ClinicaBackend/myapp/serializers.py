from rest_framework import serializers
from .models import Contacto,Medico,Paciente,Horas

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields ="all"

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields ="all"

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields ="all"
    
class HorassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horas
        fields ="_all"