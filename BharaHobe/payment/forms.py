from django import forms
from .mock_payment import MockPaymentGateway, MockPaymentError

from django import forms

class advancePaymentForm(forms.Form):
    f_payment_method = forms.ChoiceField(
        label='Payment Method',
        choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal')],
        required=True
    )
    f_credit_card_number = forms.CharField(
        label='Credit Card/PayPal Number',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Credit Card/PayPal Number'})
    )
    f_notes = forms.CharField(
        label='Additional Notes',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=False
    )
    f_amount = forms.DecimalField(label='Advance amount', min_value=0.01, required=True)
    f_card_token = forms.CharField(widget=forms.HiddenInput(), required=False)

    def clean_f_credit_card_number(self):
        credit_card_number = self.cleaned_data['f_credit_card_number']
        return credit_card_number

    def clean(self):
        cleaned_data = super().clean()
        payment_method = cleaned_data.get('f_payment_method')

        if payment_method == 'credit_card':
            cleaned_data['f_card_token'] = 'mock_card_token'

        return cleaned_data


class monthlyPaymentForm(forms.Form):
    f_order_id = forms.CharField(label='Order ID', required= True)
    f_amount = forms.DecimalField(label='Monthly amount', min_value=0.01, required= True)
    f_isSuccess = forms.BooleanField(label='Success', required=False)

class emiPaymentForm(forms.Form):
    f_order_id = forms.CharField(label='Order ID', required= True)
    f_amount = forms.DecimalField(label='EMI amount', min_value=0.01, required= True)
    f_isSuccess = forms.BooleanField(label='Success', required=False)

