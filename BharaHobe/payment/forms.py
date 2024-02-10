from django import forms

class PaymentForm(forms.Form):
    order_id = forms.CharField(label='Order ID', required= True)
    amount = forms.DecimalField(label='Amount', min_value=0.01, required= True)
    success = forms.BooleanField(label='Success', required=False)
