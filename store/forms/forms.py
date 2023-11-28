# forms.py

from django import forms


class PaymentForm(forms.Form):
    phone_number = forms.CharField()
    # amount = forms.DecimalField()
    amount = forms.DecimalField(min_value=0.01, max_digits=10, decimal_places=2, required=True)


