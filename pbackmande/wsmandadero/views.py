from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class account_user_viewset(viewsets.ModelViewSet):
    queryset = Account_User.objects.all()
    serializer_class = account_user_serializer

class mandadero_viewset(viewsets.ModelViewSet):
    queryset = Mandadero.objects.all()
    serializer_class = mandadero_serializer