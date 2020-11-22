from django.contrib import admin
from .models import Order, Product, Category, Item, Attribute, AttributeValue

admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Attribute)


class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('attribute', 'value', 'product')


admin.site.register(AttributeValue, AttributeValueAdmin)


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [AttributeValueInline, ]


admin.site.register(Product, ProductAdmin)
