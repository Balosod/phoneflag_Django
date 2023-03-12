import requests as http_requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from project.homepage import models
from project.homepage.serializers import ProductSerializer
from django_filters import rest_framework as filters
from rest_framework import generics
from .helper import ProductFilter

from django.http import JsonResponse



class FilteredProductList(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter