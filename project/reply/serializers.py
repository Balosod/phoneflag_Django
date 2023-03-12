from rest_framework import serializers
from .models import ReplyModel



class ReplySerializer(serializers.ModelSerializer):
    class Meta:
      model = ReplyModel
      fields = [ 'reply']