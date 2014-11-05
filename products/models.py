from django.db import models
from django.forms import ModelForm

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    image = models.ImageField()

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'image']  
