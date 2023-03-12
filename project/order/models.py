from django.db import models
from django.conf import settings
from project.homepage.models import Product

class Order(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name = "ordering", on_delete=models.CASCADE,null = False)
    
    def __str__(self):
        return self.owner.email