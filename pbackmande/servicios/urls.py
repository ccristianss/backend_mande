from django.urls import path, include
from rest_framework import routers
from .models import *
from .views import *

router = routers.DefaultRouter()
router.register(r'servicios', servicios_viewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace= 'rest_framework')),
]