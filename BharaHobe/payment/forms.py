from django import forms

class paymentForm(forms.Form):
    f_order_id = forms.CharField(label='Order ID', required= True)
    f_amount = forms.DecimalField(label='Amount', min_value=0.01, required= True)
    f_isSuccess = forms.BooleanField(label='Success', required=False)

class advancePaymentForm(forms.Form):
    f_order_id = forms.CharField(label='Order ID', required= True)
    f_amount = forms.DecimalField(label='Advance amount', min_value=0.01, required= True)
    f_isSuccess = forms.BooleanField(label='Success', required=False)

class monthlyPaymentForm(forms.Form):
    f_order_id = forms.CharField(label='Order ID', required= True)
    f_amount = forms.DecimalField(label='Monthly amount', min_value=0.01, required= True)
    f_isSuccess = forms.BooleanField(label='Success', required=False)

class emiPaymentForm(forms.Form):
    f_order_id = forms.CharField(label='Order ID', required= True)
    f_amount = forms.DecimalField(label='EMI amount', min_value=0.01, required= True)
    f_isSuccess = forms.BooleanField(label='Success', required=False)

