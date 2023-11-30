# forms.py

from django import forms


class PaymentForm(forms.Form):
    phone_number = forms.CharField()
    # amount = forms.DecimalField()
    amount = forms.DecimalField()


