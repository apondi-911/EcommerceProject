from django.contrib import admin


from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


# admin.py
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone']


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id','customer','order']


admin.site.register(Products, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order)

