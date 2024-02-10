from rest_framework import serializers
from .models import *

class Servicios_serializer(serializers.ModelSerializer):

    class Meta:
        model = Servicios
        fields = '__all__'