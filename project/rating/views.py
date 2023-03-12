import requests as http_requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from project.homepage.models import Product
from project.order.models import Order
from project.review.models import ProductFeedback



class Rating(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        data = request.data
        product_id = data["id"]
        rate = data['rating']
        try:
            product_instance = Product.objects.get(id = product_id)
        except:
            return Response("Product does not exist", status=status.HTTP_400_BAD_REQUEST)
        try:
            obj = Order.objects.filter(owner=user).get(product=product_instance)
        except:
            return Response("You haven't buy this product", status=status.HTTP_400_BAD_REQUEST)
        try:
            obj = ProductFeedback.objects.get(product = product_instance)
            obj.rating =  rate
            obj.save()
        except:
            ProductFeedback.objects.create(rating=rating, name = user.email, owner = user, product = product_instance)
        return Response("sucessfully rated", status=status.HTTP_200_OK)