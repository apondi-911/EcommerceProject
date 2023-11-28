from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from django_daraja.mpesa.core import MpesaClient

from store.forms.forms import PaymentForm
from store.models.customer import Customer
from django.views import View

from store.models.product import Products
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        if 'customer' in request.session:
            customer_id = request.session['customer']
            customer = Customer.objects.get(pk=customer_id)

            cart = request.session.get('cart')
            products = Products.get_products_by_id(list(cart.keys()))
            print(address, phone, customer, cart, products)

            # Save the customer first
            customer.save()

            for product in products:
                order = Order(customer=Customer(customer_id),
                              product=product,
                              price=product.price,
                              address=address,
                              phone=phone,
                              quantity=cart.get(str(product.id)))
                order.save()
        request.session['cart'] = {}

        return redirect('cart')

