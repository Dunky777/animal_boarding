from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Review(models.Model):
    name = models.CharField(max_length=33)
    pet_name = models.CharField(max_length=100)
    text = models.TextField(max_length=1333)
    star = models.IntegerField(
        validators=[
        MinValueValidator(1), 
        MaxValueValidator(5),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)