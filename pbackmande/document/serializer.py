from rest_framework import serializers
from document.models import *

class document_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'