from django.contrib.admin import actions
import json

from page.models import *
from page.serializers import CitySerializer
from rest_framework import routers, serializers, viewsets, permissions
from home.pagination import LargeResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, generics, filters
from page.serializers import *
from page.filters import *
from rest_framework import routers, serializers, viewsets, permissions
from home.pagination import LargeResultsSetPagination, CustomResultsSetPagination
from rest_framework import generics, mixins, views
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status, generics, filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


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

    @action(methods=['get'], detail=False)
    def listid(self, request):

        list = request.GET.get('listid')
        if not list:
            return Response([])
        else:
            asa = list.split(',')
            d = []


            for i in asa:
                serializer = ProductSerializer2(Product.objects.get(id=i)).data

                d.append(dict(serializer))

            return Response(d)


class TypeViewSet(generics.ListAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.filter().all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'name_ru', 'name_en']
    search_fields = ['name', 'name_ru', 'name_en']


class ProductImageViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer2
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ImageFilter
    filterset_fields = ['product']


class ReviewsViewSet(generics.ListAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['propducts']


@api_view(['POST'])
@permission_classes([AllowAny, ])
def add_reviews(request):
    # try:
    star = request.data["star"]
    text = request.data['text']
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    products = request.data['products']
    reviews = Reviews.objects.create(
        first_name=first_name,
        last_name=last_name,
        star=star,
        text=text,
        propducts_id=products,
    )
    reviews.save()

    # files = request.FILES.getlist('image')
    # for file in files:
    #     imagesreviews = ImagesReviews.objects.create(
    #         image=file,
    #         reviews=reviews
    #     ).save()
    result = {
        'status': 1,
        'msg': 'add_reviews',
        'reviews': ReviewsSerializer(reviews, many=False, context={"request": request}).data,
        # 'imagesreviews': ImagesReviewsSerializer(imagesreviews, many=False, context={"request": request}).data
    }
    return Response(result, status=status.HTTP_200_OK)

# except KeyError:
#     res = {
#         'status': 0,
#         'msg': 'error add_reviews'
#     }
#     return Response(res)
