import django_filters
from django_filters import Filter

from page.models import *




class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    city = django_filters.ModelChoiceFilter(queryset=City.objects.all())
    type = django_filters.ModelChoiceFilter(queryset=Type.objects.all())

    class Meta:
        model = Product
        fields = ['name', 'city', 'type', 'id']






class ImageFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    # city = django_filters.ModelChoiceFilter(queryset=City.objects.all())
    # type = django_filters.ModelChoiceFilter(queryset=Type.objects.all())

    class Meta:
        model = Images
        fields = ['product']