from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django_daraja.mpesa.core import MpesaClient

from store.forms.forms import PaymentForm
from store.models.product import Products
from store.views.mpesa_utils import initiate_mpesa_payment


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

        class Payment(View):
            def post(self, request):
                # Handle payment logic here, interact with M-Pesa API, and display payment form
                phone_number = '0701582114'
                amount = 1
                account_reference = 'reference'
                transaction_desc = 'Mtumba Thrift Shop'
                callback_url = 'https://de55-197-232-81-156.ngrok-free.app/callback'
                response = initiate_mpesa_payment(amount, phone_number, account_reference, transaction_desc,
                                                  callback_url)

                if response and response.get('ResponseCode') == '0':
                    # Redirect to the M-Pesa payment form
                    return redirect('mpesa_payment')  # Change this line

                else:
                    # If payment initiation failed, handle the error (you may want to show an error message)
                    return HttpResponse("Payment initiation failed. Please try again.")