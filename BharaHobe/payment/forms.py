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
        """
        Check if the provided credit card number is valid.

        Args:
            credit_card (str): Credit card number.

        Returns:
            bool: True if the credit card is valid, False otherwise.
        """
        
        if not (CreditCard(credit_card).is_valid() 
                and CreditCard(credit_card).is_luhn_valid() 
                and credit_card.isdigit() 
                and len(credit_card) == 16
                ):
            return True
        else:
            return False

    def clean_credit_card_number(self):
        """
        Clean and validate the credit card number field.

        Returns:
            str: Valid credit card number.

        Raises:
            ValidationError: If the credit card number is invalid.
        """
        credit_card = self.cleaned_data.get('f_credit_card_number')
        
        if self.is_valid_credit_card(credit_card):
            return credit_card
        raise ValidationError('Invalid credit card number')

    def clean(self):
        """
        Additional cleaning logic for the form data.

        Returns:
            dict: Cleaned form data with a mock card token when the payment method is 'credit_card'.
        """
        cleaned_data = super().clean()
        payment_method = cleaned_data.get('f_payment_method')
        
        if payment_method == 'credit_card':
            cleaned_data['f_card_token'] = 'mock_card_token'
        return cleaned_data
    
class monthlyPaymentForm(forms.Form):
    f_order_id = forms.CharField(label='Order ID', required=True)
    total_amount = forms.DecimalField(label='Total Amount', min_value=0.01, required=True)
    f_is_success = forms.BooleanField(label='Success', required=False)

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with fields for each month.

        Dynamically adds a DecimalField for each of the 6 months.
        """
        super().__init__(*args, **kwargs)

        for i in range(1, 7):
            self.fields[f'f_month_{i}'] = forms.DecimalField(
                label=f'Month {i} Amount',
                min_value=0.01,
                required=True,
            )

    def clean_total_amount(self):
        """
        Clean and validate the total amount field.

        Returns:
            Decimal: Valid total amount.

        Raises:
            ValidationError: If the total amount is invalid.
        """
        total_amount = self.cleaned_data.get('total_amount')
        if total_amount <= 0:
            raise ValidationError('Total amount must be greater than zero.')
        return total_amount

    def clean(self):
        """
        Additional cleaning logic for the form data.

        Divides the total amount equally among the 6 months.

        Returns:
            dict: Cleaned form data.
        """
        cleaned_data = super().clean()
        total_amount = cleaned_data.get('total_amount')

        monthly_share = total_amount / 6
        for i in range(1, 7):
            cleaned_data[f'f_month_{i}'] = monthly_share
        return cleaned_data

class emiPaymentForm(forms.Form):
    f_order_id = forms.CharField(label='Order ID', required= True)
    f_amount = forms.DecimalField(label='EMI amount', min_value=0.01, required= True)
    f_isSuccess = forms.BooleanField(label='Success', required=False)

