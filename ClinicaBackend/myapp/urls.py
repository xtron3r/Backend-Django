from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactoViewSet,MedicoViewSet,PacienteViewSet,HorasViewSet,UserViewSet



router = DefaultRouter()
router.register('contacto', ContactoViewSet)
router.register('medico', MedicoViewSet)
router.register('paciente', PacienteViewSet)
router.register('horas', HorasViewSet)
router.register('user' , UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
