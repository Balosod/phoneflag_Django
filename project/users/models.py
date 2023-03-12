import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from .managers import CustomUserManager
from django.core.validators import RegexValidator


class User(AbstractUser):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

    
    GENDER = [
        (MALE, "MALE"),
        (FEMALE, "FEMALE"),
        (OTHER, "OTHER"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=20, unique=False, blank=True, null=True)
    location = models.CharField(max_length=300, blank=True, null=True)
    shipping_address = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True)
    date_of_birth = models.DateTimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null = True, blank=True) 
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=20, choices = GENDER, default=OTHER,)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
