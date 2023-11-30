from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django_daraja.mpesa.core import MpesaClient

from store.forms.forms import PaymentForm
from store.models.product import Products
# from store.views.mpesa_utils import initiate_mpesa_payment


class Cart(View):

    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'products': products})

    def post(self, request):
        action = request.POST.get('action')
        product_id = request.POST.get('product')

        print(f"Received action: {action}, product_id: {product_id}")
        if action and product_id:
            cart = request.session.get('cart', {})

            if action == '+':
                cart[product_id] = cart.get(product_id, 0) + 1
            elif action == '-':
                if product_id in cart:
                    cart[product_id] -= 1
                    if cart[product_id] <= 0:
                        del cart[product_id]

            request.session['cart'] = cart
            return redirect('cart')  # Redirect to the cart page after processing the form

