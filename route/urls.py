from page.views import *

from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from home import settings

router = routers.DefaultRouter()

router.register(r'city', CityViewSet)
router.register(r'type', TypeViewSet)
router.register(r'product', ProductViewSet)
router.register(r'productimags', ProductImageViewSet)

urlpatterns = [

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
