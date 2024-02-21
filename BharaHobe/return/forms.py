from django import forms
from .models import ReturnRequest

class ReturnRequestForm(forms.ModelForm):
    class Meta:
        model = ReturnRequest
        fields = ['reason', 'desired_resolution', 'supporting_evidence']