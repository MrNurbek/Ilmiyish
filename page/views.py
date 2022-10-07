from page.models import *
from page.serializers import CitySerializer
from rest_framework import routers, serializers, viewsets, permissions
from home.pagination import LargeResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, generics, filters
from page.serializers import *
from page.filters import *


class CityViewSet(generics.ListAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.filter().all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'name_ru', 'name_en']
    search_fields = ['name', 'name_ru', 'name_en', 'text']

    # def get_queryset(self):
    #     if self.request.GET.get("parent"):
    #         return City.objects.filter(parent=self.request.GET.get("parent")).all()
    #     return City.objects.all()
    # def get_queryset(self):
    #     if self.request.GET.get("parent"):
    #         return City.objects.filter(parent=self.request.GET.get("parent")).all()
    #     return City.objects.filter(parent=None).all()


class ProductViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'text']

    def get_serializer_class(self):
        if self.action == "list":
            return ProductSerializer
        else:
            return ProductDetailSerializer


class TypeViewSet(generics.ListAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.filter().all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'name_ru', 'name_en']
    search_fields = ['name', 'name_ru', 'name_en']


class ProductImageViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductImageSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ProductFilter


