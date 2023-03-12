import requests as http_requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from project.homepage import models
from project.homepage.serializers import ProductSerializer
from django.db.models import Q


class Search(APIView):
    def post(self, request):
        data = request.data
        search_by = data["search"]
        print(search_by)
        query_set = models.Product.objects.filter(Q(name__icontains = search_by)|
                                                  Q(category__icontains = search_by)|
                                                  Q(brand__icontains = search_by))
        serializer = ProductSerializer(query_set,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
