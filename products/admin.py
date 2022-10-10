from django.contrib import admin
from .models import Product, Category
from django.utils.html import format_html

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}"  width="100" height="100"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'image_tag',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
