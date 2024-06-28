from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=254, required=False)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email']
