from rest_framework import routers
from .api import *
from django.urls import include, path


router = routers.DefaultRouter()

router.register('api/aspirantes', AspirantesViewSet, 'aspirantes'),
router.register('api/afinidadMagica',AfinidadMagicaViewSet, 'afinidadMagica'),
router.register('api/grimorios', GrimorioViewSet, 'grimorios'),

#Modificar solo lectura

urlpatterns = router.urls