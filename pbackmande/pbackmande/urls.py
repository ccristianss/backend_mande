"""
URL configuration for pbackmande project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.documentation import include_docs_urls
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from servicios.models import *
from servicios.views import *
from document.models import *
from document.views import *
from wsmandadero.models import *
from wsmandadero.views import *
from vehicle.views import *
from vehicle.models import *


router = routers.DefaultRouter()
router.register(r'document', view_document)
router.register(r'account_user', account_user_viewset)
router.register(r'mandadero', mandadero_viewset)
router.register(r'servicios', servicios_viewset)
router.register(r'vehicle', views_vehicle)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', include_docs_urls(title='documentation of Api'))
]
