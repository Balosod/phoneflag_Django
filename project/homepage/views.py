import requests as http_requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from . import models
from .serializers import ProductSerializer


class HomePage(APIView):
    def get(self, request):
        output_cat = {}
        output_data = {"sponsored":"","todays_deals":"","best_sellers":"","category":[output_cat]}
        query_set = models.Product.objects.all()
        query_set1 = models.Product.objects.filter(sponsored = True)
        query_set2 = models.Product.objects.filter(todays_deals = True)
        query_set3 = models.Product.objects.filter(best_sellers = True)
        serializer1 = ProductSerializer(query_set1,many=True)
        serializer2 = ProductSerializer(query_set2,many=True)
        serializer3 = ProductSerializer(query_set3,many=True)
        output_data["sponsored"] = serializer1.data
        output_data["todays_deals"] = serializer2.data
        output_data["best_sellers"] = serializer3.data
        for item in query_set:
            if item.category in output_cat:
                output_cat[item.category] = output_cat[item.category]+1
            else:
                output_cat[item.category] = 1
        return Response(output_data, status=status.HTTP_200_OK)