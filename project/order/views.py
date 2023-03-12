import requests as http_requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .import models
from project.homepage.models import Product
from project.homepage.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated


class Order(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data = request.data
        product_id = data["id"]
        user =  request.user
        product_instance = Product.objects.get(id = product_id)
        create_checkout = models.Order.objects.create(owner= user,product=product_instance)
        return Response("successfully checkout", status=status.HTTP_200_OK)