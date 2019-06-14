from django.db import models
from django.contrib.auth.models import User
from account.models import UserProfile


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image = models.FileField()
    description = models.TextField()
    date = models.DateTimeField()
    product_owner_info = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
