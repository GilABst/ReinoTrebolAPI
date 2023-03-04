from .models import *
from rest_framework import viewsets, permissions
from .serializer import *


class AspirantesViewSet(viewsets.ModelViewSet):
    queryset = Aspirante.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AspiranteSerializar

class AfinidadMagicaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Afinidad_Magicas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AfinidadMagicasSerializer

class GrimorioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Grimorios.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GrimoriosSerializer