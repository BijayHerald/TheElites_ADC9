from django.contrib import admin
from .models import Category, Product


# Register your models here.

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}



# # class ProductAdmin(admin.ModelAdmin):
# #     list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'created_at', 'updated_at']
# #     list_filter = ['available', 'created_at', 'updated_at', 'category']
# #     list_editable = ['price', 'stock', 'available']
# #     prepopulated_fields = {'slug': ('name',)}


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Product, ProductAdmin)
