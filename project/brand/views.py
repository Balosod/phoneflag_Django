import requests as http_requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from project.homepage import models
from project.homepage.serializers import ProductSerializer


class Brand(APIView):
    def get(self,request,name):
        query_set = models.Product.objects.filter(brand=name)
        serializer = ProductSerializer(query_set,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)