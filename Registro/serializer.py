from rest_framework import serializers
from .models import *
from .utils import seleccionar_grimorio_random


class GrimoriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grimorios
        fields = ('id','categoria', 'trebol')
        read_only_fields = ('id','categoria', 'trebol')

class AfinidadMagicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Afinidad_Magicas
        fields = ('id','afinidadMagica',)
        read_only_fields = ('id','afinidadMagica',)

class AspiranteSerializar(serializers.ModelSerializer):

    grimorio = serializers.SerializerMethodField()

    def get_grimorio(self, obj):
        if obj.status ==  True:
            random = seleccionar_grimorio_random()
            return random
        else:
            return 0

    class Meta:
        model = Aspirante
        fields = ('id', 'nombre', 'apellido', 'identificacion',
                  'edad', 'afinidadMagica', 'grimorio', 'status')
        read_only_fields = ('grimorio',)
