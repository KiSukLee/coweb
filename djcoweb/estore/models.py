from django.db import models
from logreg.models import User

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    price = models.DecimalField(decimal_places = 2, max_digits = 4)
    quantity = models.IntegerField()

class Product(models.Model):
    product_id = models.IntegerField()
    quantity = models.IntegerField()

class Cart(models.Model):
    user = models.ForeignKey(User, related_name = "carts", on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name = "carts")
    total = models.DecimalField(decimal_places = 2, max_digits = 7)