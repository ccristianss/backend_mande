from rest_framework import serializers
from vehicle.models import *

class vehicle_serializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'