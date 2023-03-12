import requests as http_requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from project.homepage import models
from project.homepage.serializers import ProductSerializer
from project.review.serializers import ReviewSerializer
from project.review.models import ProductFeedback
from project.order.models import Order
from django.contrib.auth import get_user_model
from project.users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

User = get_user_model()
        
        
class Preview(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,id):
        total_ratings = 0
        ratings_average = 0
        total_product_sold = 0
        modify_ratings = {"5":0,"4":0,"3":0,"2":0,"1":0}
        output_data = {"product":"","user":"","reviews":"","ratings":modify_ratings,"total_reviews":"","total_ratings":"","ratings_average":"","total_product_sold":""}
        user_query_set = User.objects.filter(email = request.user.email).get()
        serializer1 = UserSerializer(user_query_set)
        output_data["user"] = serializer1.data
        try:
            query_set1 = models.Product.objects.get(id=id)
        except:
            return Response("product id does not exit", status=status.HTTP_400_BAD_REQUEST)    
        serializer2 = ProductSerializer(query_set1)
        output_data["product"] = serializer2.data
        try:
            query_set2 = ProductFeedback.objects.filter(product=query_set1)
            serializer3 = ReviewSerializer(query_set2,many=True)
            output_data["reviews"] = serializer3.data
            output_data["total_reviews"] = query_set2.count()
        except:
            pass
        try:
            ratings  = ProductFeedback.objects.filter(product = query_set1)
            divisor = 0
            for rate in ratings:
                divisor +=1
                if rate.rating == "5":
                    modify_ratings["5"] = modify_ratings["5"]+1
                    total_ratings+=5
                elif rate.rating == "4":
                    modify_ratings["4"] = modify_ratings["4"]+1
                    total_ratings+=4
                elif rate.rating == "3":
                    modify_ratings["3"] = modify_ratings["3"]+1
                    total_ratings+=3
                elif rate.rating == "2":
                    modify_ratings["2"] = modify_ratings["2"]+1
                    total_ratings+=2
                elif rate.rating == "1":
                    modify_ratings["1"] = modify_ratings["1"]+1
                    total_ratings+=1
            ratings_average += round((total_ratings/divisor),1)
        except:
            pass
        try:
            obj = Order.objects.filter(product=query_set1).count()
            total_product_sold += obj
        except:
            pass
        output_data["ratings_average"] = ratings_average
        output_data["total_ratings"] = total_ratings
        output_data["total_product_sold"] = total_product_sold
        return Response(output_data, status=status.HTTP_200_OK)
        