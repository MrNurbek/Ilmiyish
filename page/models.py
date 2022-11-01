from django.db import models
# from location_field.models.spatial import LocationField
from location_field.models.plain import PlainLocationField


# from django.contrib.gis.geos import Point


class City(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    name_ru = models.CharField(max_length=255, null=True, blank=True)
    name_en = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="profession", default='users/default.png')
    text = models.CharField(max_length=1024, null=True, blank=True)
    lon = models.FloatField(max_length=512, null=True, blank=True)
    lat = models.FloatField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    name_ru = models.CharField(max_length=255, null=True, blank=True)
    name_en = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="profession", default='users/default.png')
    marker = models.ImageField(upload_to="profession", null=True, blank=True)
    parent = models.ForeignKey('self', related_name='childs', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Images(models.Model):
    image = models.ImageField(upload_to="profession", default='users/default.png', null=True, blank=True)
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE, null=True)


class ImagesReviews(models.Model):
    image = models.ImageField(upload_to="profession", default='users/default.png', null=True, blank=True)
    reviews = models.ForeignKey("Reviews", related_name='images', on_delete=models.CASCADE, null=True)


class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    star = models.IntegerField(default=0, null=True, blank=True)
    text = models.CharField(max_length=5024, null=True, blank=True)
    city = models.ForeignKey(City, related_name='product', on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(Type, related_name='product1', on_delete=models.CASCADE, null=True)
    lon = models.FloatField(max_length=512, null=True, blank=True)
    lat = models.FloatField(max_length=512, null=True, blank=True)
    open = models.TimeField(blank=True, null=True)
    closed = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    star = models.IntegerField(default=0, null=True, blank=True)
    text = models.CharField(max_length=512, null=True, blank=True)
    propducts = models.ForeignKey('Product', related_name='reviews', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.text
# dfs
