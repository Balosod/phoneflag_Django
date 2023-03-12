from django_filters import rest_framework as filters
from project.homepage.models import Product

class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="off_price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="off_price", lookup_expr='lte')
    class Meta:
        model = Product
        fields = ['category','location','first_condition','color','brand','min_price', 'max_price',]