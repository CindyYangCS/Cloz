from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Garment(models.Model):
    class Type(models.TextChoices):
        TOP = "TOP", "Top"
        BOTTOMS = "BOTTOMS", "Bottoms"
        SHOES = "SHOES", "Shoes"
        ACCESSORIES = "ACCESSORIES", "Accessories" 

    type = models.CharField(max_length=20, choices=Type.choices)
    brand = models.CharField(max_length=150)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='clothes', blank=True, null=True)
    date_purchased = models.DateField(blank=True, null=True)
    thrifted = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.name}"