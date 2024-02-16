from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Profile


class profilePageForm(forms.ModelForm):
    """
    Form for updating the profile page of a user.
    """
    class Meta:
        model = Profile
        fields = ('m_bio', 'm_profile_pic', 'm_email', 'm_facebook_url')  # Use correct field names

        widgets = {
            'm_bio': forms.Textarea(attrs={'class': 'form-control'}),
            'm_profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'm_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'm_facebook_url': forms.URLInput(attrs={'class': 'form-control'}),      
        }


class editProfileForm(UserChangeForm):
    """
    Form for editing user profile details.
    """
    f_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    f_last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    f_username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    f_last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    f_is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    f_is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    f_is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    f_date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'last_login',
                  'is_superuser', 'is_staff', 'is_active', 'date_joined')
