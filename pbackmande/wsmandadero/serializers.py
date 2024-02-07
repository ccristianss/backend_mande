from rest_framework import serializers
from .models import *

class account_user_serializer(serializers.ModelSerializer):

    class Meta:
        model = Account_User
        fields = '__all__'

class mandadero_serializer(serializers.ModelSerializer):

    class Meta:
        model = Mandadero
        fields = '__all__'