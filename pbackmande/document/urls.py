from django.urls import path, include
from rest_framework import routers
from document.models import *
from document.views import *

router = routers.DefaultRouter()
router.register(r'document', view_document)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
