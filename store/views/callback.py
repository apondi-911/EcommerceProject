import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from store.models import Order  # Adjust import as needed


@csrf_exempt
@require_POST
def callback(request):
    try:
        # Get the raw data from the request body
        callback_data_raw = request.body.decode('utf-8')

        # Parse the JSON data
        callback_data = json.loads(callback_data_raw)

        order_id = get_order_id_from_callback_data(callback_data)

        if order_id:
            # Update order status based on callback data
            update_order_status(order_id, callback_data)

        return HttpResponse("Callback received.")
    except json.JSONDecodeError as e:
        # Handle JSON decoding error
        return HttpResponse(f"Error decoding JSON: {e}", status=400)


def get_order_id_from_callback_data(callback_data):
    # Extract order ID from callback data
    # Adjust this based on the actual structure of your callback data
    return callback_data.get('order_id')


def update_order_status(order_id, callback_data):
    # Update order status based on callback data
    # You'll need to adjust this based on your actual order model and callback data
    order = Order.objects.get(pk=order_id)

    if callback_data.get('payment_status') == 'completed':
        order.status = True  # Assuming your Order model has a 'status' field
        # You might want to update other fields based on the callback data
        # For example, storing Mpesa transaction ID, amount, etc.
    else:
        order.status = False

    order.save()
