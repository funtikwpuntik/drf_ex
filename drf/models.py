from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE


# Create your models here.


class ApiUser(AbstractUser):
    type = models.CharField(max_length=32)
    ...

    def __str__(self):
        return f"{self.username}"


class Warehouse(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.id}: {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=128)
    count = models.PositiveIntegerField(default=0)
    warehouse = models.ForeignKey(Warehouse, related_name="products", on_delete=CASCADE)

    def __str__(self):
        return f"{self.id}: {self.warehouse.name}. Product name: {self.name}."


class Order(models.Model):
    product = models.ForeignKey(Product, related_name="orders", on_delete=CASCADE)
    user = models.ForeignKey(ApiUser, related_name="orders", on_delete=CASCADE)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name}"
