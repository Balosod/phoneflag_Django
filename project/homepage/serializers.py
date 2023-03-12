from rest_framework import serializers
from .models import Product,ProductImages



class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
      model = ProductImages
      fields = ['id', 'img']
      
      
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#       model = Product
#       fields = "__all__"
      
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImagesSerializer(many=True,read_only=True)

    class Meta:
        model = Product
        fields = ['id','name','category','brand','first_condition',
                  'second_condition','internal_storage','screen_size',
                  'battery_capacity','operating_system','weight','color','description','minimum_order',
                  'discount_price','off_price','sold_out','sponsored','location','images']