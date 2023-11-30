from django.shortcuts import redirect, render
from django.views import View

from store.models.customer import Customer
from store.models.orders import Order
from store.models.product import Products
from store.views.utils import calculate_cart_total, get_cart_items


class CheckOut(View):
    def get(self, request):
        # Ensure that the 'cart' attribute is present in the session
        cart = request.session.get('cart', {})
        if not cart:
            return redirect('cart')

        cart_items = get_cart_items(cart)
        cart_total = calculate_cart_total(cart)
        return render(request, 'cart.html', {'cart_items': cart_items, 'cart_total': cart_total})

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        # Ensure that the 'cart' attribute is present in the session
        cart = request.session.get('cart', {})
        if not cart:
            return redirect('cart')

        if 'customer' in request.session:
            customer_id = request.session['customer']

            try:
                # Attempt to get the existing customer
                customer = Customer.objects.get(pk=customer_id)
            except Customer.DoesNotExist:
                # If the customer does not exist, create a new one
                customer = Customer.objects.create(pk=customer_id)

            products = Products.get_products_by_id(list(cart.keys()))
            print(address, phone, customer, cart, products)

            try:
                for product in products:
                    order = Order(customer=customer,
                                  product=product,
                                  price=product.price,
                                  address=address,
                                  phone=phone,
                                  quantity=cart.get(str(product.id)))
                    order.save()
            except Exception as e:
                print(f"Error creating orders: {e}")

            # Clear the cart after successful order creation
            request.session['cart'] = {}
            return redirect('cart')

        # Handle the case where 'customer' is not in the session
        return redirect('login')
