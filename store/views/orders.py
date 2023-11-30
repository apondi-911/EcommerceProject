from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware

class OrderView(View):
    def get(self , request ):
        customer_id = request.session.get('customer')
        if not customer_id:
            # Handle the case where customer ID is not set in the session
            return redirect('login')  # Redirect to the login page or homepage

        customer = Customer.objects.get(pk=customer_id)
        orders = Order.get_orders_by_customer(customer)
        return render(request, 'orders.html', {'orders': orders})