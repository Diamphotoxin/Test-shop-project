from django.db import models
from django.core.validators import RegexValidator, MaxLengthValidator


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    telephone = RegexValidator(r'^\d+$', 'Only numeric characters are allowed.')

    customer_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15, validators=[telephone, MaxLengthValidator])
    items = models.ManyToManyField('Item')

    def __str__(self):
        return self.id


class Item(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
