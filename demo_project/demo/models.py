from django.db import models

# Create your models here.
class Product(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_quantity = models.IntegerField()
    price = models.FloatField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.prod_name
