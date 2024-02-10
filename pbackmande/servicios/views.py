from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class servicios_viewset(viewsets.ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = Servicios_serializer
