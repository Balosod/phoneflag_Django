from django.contrib import admin
from  . models import Product, ProductImages



class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
 
    class Meta:
       model = Product

