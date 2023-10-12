from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
    ]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "designation",
        "title",
        "material",
        "units_of_measure",
        "price_for_unit",
        "in_stock",
    ]
    list_filter = [
        "is_in_stock",
        "material",
        "designation",
    ]
    search_fields = [
        "material",
        "designation",
    ]
    ordering = [
        "designation",
        "title",
        "material",
    ]
