from django.urls import path, include
from rest_framework import routers
from .models import *
from .views import *


router = routers.DefaultRouter()
router.register(r'document', servicios_viewset)

urlpatterns = [
    path('v2/', include(router.urls)),
]