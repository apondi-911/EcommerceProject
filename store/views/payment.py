from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django_daraja.mpesa.core import MpesaClient
from store.forms.forms import PaymentForm


# @csrf_exempt
# def mpesa_callback(request):
#     # Process Mpesa callback data
#     return HttpResponse("Callback received.")


def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            client = MpesaClient()
            phone_number = form.cleaned_data['phone_number']

            # Convert the amount to an integer
            amount_str = form.cleaned_data['amount']
            try:
                amount = int(amount_str)
            except ValueError:
                # Handle the case where the amount is not a valid integer
                return render(request, 'failed.html', {'error_message': 'Invalid amount'})

            account_reference = 'reference'
            transaction_desc = 'Description'
            callback_url = 'https://api.darajambili.com/express-payment'
            response = client.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
            return HttpResponse(response)
        return render(request, 'failed.html')
    else:
        return render(request, 'failed.html')
