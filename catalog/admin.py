from django.contrib import admin
from .models import Order, Product, Category, Item

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Item)

