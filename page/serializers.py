from django.db.models import Avg
# from django.urls import path, include

from rest_framework import serializers
from django.db.models import Avg, Count
from page.models import City, Type, Images, Product, Reviews


class CitySerializer(serializers.ModelSerializer):
    # childs = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = ["id", "image", "name", "text", "lon", "lat"]

    def get_name(self, obj):
        request = self.context.get("request")
        data = request.GET if hasattr(request, 'GET') else {}
        lang = data['lang'] if 'lang' in data else 'uz'

        if lang == "ru":
            return obj.name_ru
        elif lang == "en":
            return obj.name_en
        return obj.name

    # def get_childs(self, obj):
    #     return CitySerializer(obj.childs, many=True, ).data

    # def get_name(self, obj):
    #
    #     lang = str(self.context["request"])
    #
    #     a = lang.split('/')
    #
    #     if a[1] == "ru":
    #         return obj.name_ru
    #     elif a[1] == "en":
    #         return obj.name_en
    #     else:
    #         return obj.name
    #
    # def get_parent(self, obj):
    #     print(obj,'sssssssssss')
    #     return City2Serializer(obj.parent, many=True).data


class TypeSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Type
        fields = ["id", "image", "name"]

    def get_name(self, obj):
        request = self.context.get("request")
        data = request.GET if hasattr(request, 'GET') else {}
        lang = data['lang'] if 'lang' in data else 'uz'

        if lang == "ru":
            return obj.name_ru
        elif lang == "en":
            return obj.name_en
        return obj.name


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    review_avg = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'star', 'images', 'city', 'type', 'review_avg', 'text', 'lon', 'lat', 'open', 'closed']

    def get_images(self, obj):
        images = Images.objects.filter(product=obj).first()
        if images:
            return ImagesSerializer(images, many=False, context={'request': self.context['request']}).data
        return None

    def get_review_avg(self, obj):
        return Reviews.objects.filter(propducts=obj).aggregate(avg_rating=Avg('star'))["avg_rating"]


class ProductImageSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'images']

    def get_images(self, obj):
        images = Images.objects.filter(product=obj).all()
        return ImagesSerializer(images, many=True, context={'request': self.context['request']}).data


class ProductDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    review = serializers.SerializerMethodField()
    review_avg = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'star', 'images', 'city', 'type', 'review', 'text', "review_avg", 'lon', 'lat', 'open',
                  'closed']

    def get_images(self, obj):
        images = Images.objects.filter(product=obj).all()
        return ImagesSerializer(images, many=True, context={'request': self.context['request']}).data

    def get_review(self, obj):
        review = Reviews.objects.filter(propducts=obj).first()
        if review:
            return ReviewsSerializer(review, many=False, context={'request': self.context['request']}).data
        return None

    def get_review_avg(self, obj):
        return Reviews.objects.filter(propducts=obj).aggregate(avg_rating=Avg('star'))['avg_rating']


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['text', 'date', 'propducts', 'star']
