from django.db import models
from django.conf import settings
from project.review.models import ProductFeedback


class ReplyModel(models.Model):
    reply = models.CharField(max_length=300)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(ProductFeedback, related_name = "replys", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.owner.email