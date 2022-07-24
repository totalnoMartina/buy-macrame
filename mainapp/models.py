from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=150)
    sku = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=8,
            validators=[MinValueValidator(0)]
            )
    image = models.ImageField(null=True, blank=True)

    
    def __str__(self):
        return self.name


class BoughtItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name