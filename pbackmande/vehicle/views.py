from rest_framework import viewsets
from vehicle.models import *
from .serializers import *


class views_vehicle(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = vehicle_serializers    # Asegúrate de que este sea el nombre correcto de tu serializador
