from django import forms
from django.core.exceptions import ValidationError
from creditcard import CreditCard 


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

    def is_valid_credit_card(self, credit_card):
        try:
            card = CreditCard(credit_card)
            return card.is_valid() and card.is_luhn_valid()
        except ValueError:
            return False

    def clean_credit_card_number(self):
        credit_card = self.cleaned_data.get('f_credit_card_number')
        if not self.is_valid_credit_card(credit_card):
            raise ValidationError('Invalid credit card number')
        return credit_card

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

