from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    address = models.CharField(max_length=300)
    description = models.TextField()
    hotel_image = models.ImageField(upload_to='photos/hotels', blank=True)
    price = models.IntegerField() 
    def __str__(self) -> str:
        return self.hotel_name 


class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()  
