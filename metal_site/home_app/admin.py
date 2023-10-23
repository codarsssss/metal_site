from django.contrib import admin
from .models import Product, Category, Feedback


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
    ]
    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 10


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
    list_per_page = 10


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "contact_number",
        "email",
        "time_create",
    ]
    list_filter = ["contact_number", "time_create"]
    search_fields = [
        "contact_number",
        "email",
    ]
    ordering = ["time_create", "contact_number"]
    list_per_page = 10
