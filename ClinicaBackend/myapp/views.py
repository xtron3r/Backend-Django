from rest_framework import viewsets
from .models import Contacto,Medico,Paciente,Horas
from .serializers import ContactoSerializer, MedicoSerializer,PacienteSerializer,HorassSerializer

# Create your views here.
class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class HorasViewSet(viewsets.ModelViewSet):
    queryset = Horas.objects.all()
    serializer_class = HorassSerializer