from document.models import *
from .serializer import *
from rest_framework import viewsets


# Create your views here.
class view_document(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = document_serializer
