from django.db import models
from django.conf import settings
from project.homepage.models import Product

class ProductFeedback(models.Model):
    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"
    _5 = "5"
    
    RATINGS = [
        (_1, "1"),
        (_2, "2"),
        (_3, "3"),
        (_4, "4"),
        (_5, "5"),
    ]
    rating = models.CharField(max_length=5,choices = RATINGS,null =True,blank=True)
    name = models.CharField(max_length=100,null =True,blank=True)
    review = models.CharField(max_length=300,null =True,blank=True)
    liked = models.IntegerField(default = 0)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.owner.email