from store.models.product import Products


def calculate_cart_total(cart):
    total = 0
    for product_id, quantity in cart.items():
        product = Products.objects.get(pk=product_id)
        total += product.price * quantity
    return total


# Assuming this function is defined in a file named utils.py

def get_cart_items(cart):
    items = []
    for product_id, quantity in cart.items():
        product = Products.objects.get(pk=product_id)
        items.append({'product': product, 'quantity': quantity})
    return items
