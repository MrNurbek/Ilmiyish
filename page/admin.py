from django.contrib import admin
from page.models import *


# Register your models here.
class ImagesInline(admin.TabularInline):
    model = Images


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    # list_editable = ['flash_sale', 'mega_sale', 'home_sale']
    inlines = [ImagesInline]
    # filter_horizontal = ('color', 'size')


class ImagesAdmin(admin.ModelAdmin):
    # list_display = (' image ')
    # sortable_by = ('image')
    search_fields = ['image']


admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(City)
admin.site.register(Type)
admin.site.register(Reviews)
