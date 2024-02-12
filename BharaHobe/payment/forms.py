from django import forms

class advancePaymentForm(forms.Form):
    f_order_id = forms.CharField(label='Order ID', required=True, max_length=50)
    f_amount = forms.DecimalField(label='Advance amount', min_value=0.01, required=True)
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

    def clean_f_credit_card_number(self):
        credit_card_number = self.cleaned_data['f_credit_card_number']
        if credit_card_number == "123":
            self.cleaned_data['f_isSuccess'] = True
            return credit_card_number
        else:
            raise forms.ValidationError('Invalid Credit Card/PayPal Number')

    def clean_f_amount(self):
        amount = self.cleaned_data['f_amount']
        return amount


class monthlyPaymentForm(forms.Form):
    f_order_id = forms.CharField(label='Order ID', required= True)
    f_amount = forms.DecimalField(label='Monthly amount', min_value=0.01, required= True)
    f_isSuccess = forms.BooleanField(label='Success', required=False)

class emiPaymentForm(forms.Form):
    f_order_id = forms.CharField(label='Order ID', required= True)
    f_amount = forms.DecimalField(label='EMI amount', min_value=0.01, required= True)
    f_isSuccess = forms.BooleanField(label='Success', required=False)

