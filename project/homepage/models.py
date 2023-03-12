from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator



class Product(models.Model):
    HANDPHONE = "handphone"
    TABLET = "tablet"
    LAPTOP = "laptop"
    COMPUTER = "computer"
    TELEVISION = "television"
    
    CATEGORY = [
        (HANDPHONE, "HANDPHONE"),
        (TABLET, "TABLET"),
        (LAPTOP, "LAPTOP"),
        (COMPUTER, "COMPUTER"),
        (TELEVISION, "TELEVISION"),
    ]
    
    APPLE = "apple"
    XIAOMI = "xiaomi"
    SAMSUNG = "samsung"
    ASUS = "asus"
    REALME = "realme"
    HUAWEL = "huawel"
    
    BRAND = [
        (APPLE, "APPLE"),
        (XIAOMI, "XIAOMI"),
        (SAMSUNG, "SAMSUNG"),
        (ASUS, "ASUS"),
        (REALME, "REALME"),
        (HUAWEL, "HUAWEL"),
    ]
    
    BRAND_NEW = "new"
    SECOND = "second"

    
    FIRST_CONDITION = [
        (BRAND_NEW, "BRAND_NEW"),
        (SECOND, "SECOND"),
    ]
    
    _16GB = "16GB"
    _32GB = "32GB"
    _64GB = "64GB"
    _128GB = "128GB"
    _256GB = "256GB"
    _512GB = "512GB"
    
    INTERNAL_STORAGE = [
        (_16GB, "16GB"),
        (_32GB, "32GB"),
        (_64GB, "64GB"),
        (_128GB, "128GB"),
        (_256GB, "256GB"),
        (_512GB, "512GB"),
    ]
    
    ANDROID = "android"
    APPLE_IOS = "apple"

    
    OPERATING_SYSTEM = [
        (ANDROID, "ANDROID"),
        (APPLE_IOS, "APPLE_IOS"),
    ]
    
    name =  models.CharField(max_length = 200)
    category =  models.CharField(max_length = 20,choices = CATEGORY)
    brand =  models.CharField(max_length = 20,choices =BRAND)
    first_condition =  models.CharField(max_length = 20, choices=FIRST_CONDITION)
    second_condition =  models.CharField(max_length = 200)
    internal_storage =  models.CharField(max_length = 20, choices = INTERNAL_STORAGE)
    screen_size =  models.CharField(max_length = 200)
    battery_capacity =  models.CharField(max_length = 200)
    operating_system =  models.CharField(max_length = 20, choices = OPERATING_SYSTEM)
    weight =  models.CharField(max_length = 20,blank=True,null= True)
    color =  models.CharField(max_length = 200,blank=True,null= True)
    description =  models.CharField(max_length = 200)
    minimum_order =  models.CharField(max_length = 200)
    discount_price= models.DecimalField(max_digits=10, decimal_places=2)
    off_price =  models.DecimalField(max_digits=10, decimal_places=2, blank=True,null= True)
    sold_out =  models.PositiveIntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    sponsored = models.BooleanField(default=False)
    todays_deals = models.BooleanField(default=False)
    best_sellers = models.BooleanField(default=False)
    location =  models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
    
    
    
class ProductImages(models.Model):
    img = models.ImageField()
    product = models.ForeignKey(Product,related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.img}"
    