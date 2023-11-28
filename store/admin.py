from django.contrib import admin

from .models.C2BPayments import C2BPayments
from .models.Online import Online
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


class OnlineAdmin(admin.ModelAdmin):
    list_display = ("PhoneNumber", "Amount", "MpesaReceiptNumber", "TransactionDate")


class C2BPaymentsAdmin(admin.ModelAdmin):
    list_display = ("MSISDN", "TransAmount", "TransID", "TransTime")


# Register your models here.
admin.site.register(Products, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order)
admin.site.register(C2BPayments, C2BPaymentsAdmin)
admin.site.register(Online, OnlineAdmin)
