import requests as http_requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .import models
from project.homepage.models import Product
from project.homepage.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from project.review.models import ProductFeedback




class Reply(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        data = request.data
        review_id = data["id"]
        try:
            reply = data['reply']
            try:
                review_instance = ProductFeedback.objects.get(id = review_id)
            except:
                return Response("Review does not exist", status=status.HTTP_400_BAD_REQUEST)
            create_reply = models.ReplyModel.objects.create(reply = reply, owner= user,review=review_instance)
            return Response("reply created", status=status.HTTP_200_OK)
        except:
            pass
        try:
            liked = data['liked']
            try:
                review_instance = ProductFeedback.objects.filter(id = review_id)
            except:
                return Response("Review does not exist", status=status.HTTP_400_BAD_REQUEST)
            like=review_instance.values()[0]["liked"]
            review_instance.update(liked=like+1)
            return Response("Review liked", status=status.HTTP_200_OK)
        except:
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)