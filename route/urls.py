from page.views import *

from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'city', CityViewSet)
router.register(r'type', TypeViewSet)
router.register(r'product', ProductViewSet)
router.register(r'productimags', ProductImageViewSet)

urlpatterns = [

]

urlpatterns += router.urls
