from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name


class Product(models.Model):
    # movie_id = models.CharField(max_length=250, blank=True)
    name = models.CharField(max_length=250)
    desc = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=True)
    img = models.ImageField(upload_to='gallery')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
