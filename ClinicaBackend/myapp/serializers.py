from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import Contacto,Medico,Paciente,Horas

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

class HorassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horas
        fields ="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"