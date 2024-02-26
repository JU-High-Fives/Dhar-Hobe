from django import forms
from . models import ReturnRequest

class ReturnRequestForm(forms.ModelForm):
    """
    Form class for creating a return request.

    This form is based on the ReturnRequest model and allows users to submit
    return requests with specified fields.

    Attributes:
        reason: A choice field for selecting the reason for return.
        desired_resolution: A field for specifying the desired resolution.
        supporting_evidence: A text field for providing supporting evidence.
    """
    class Meta:
        """
        Meta class specifying the model and fields for the form.
        """
        model = ReturnRequest  # Specifies the model used for the form
        fields = ['reason', 'desired_resolution', 'supporting_evidence']  # Specifies the fields to be included in the form
