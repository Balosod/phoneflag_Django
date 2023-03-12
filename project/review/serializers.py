from rest_framework import serializers
from .models import ProductFeedback
from project.reply.serializers import ReplySerializer



class ReviewSerializer(serializers.ModelSerializer):
    replys = ReplySerializer(many=True,read_only=True)
    class Meta:
      model = ProductFeedback
      fields = ['id', 'name','review','rating','liked','replys']