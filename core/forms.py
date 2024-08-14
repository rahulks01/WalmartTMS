from django import forms
from .models import User, TrailerRentalRequest
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, label="Login as")

class TrailerRentalRequestForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = TrailerRentalRequest
        fields = ['owner_name', 'company_name', 'contact_info', 'trailer_details', 'username', 'password']

class DriverCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(DriverCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Driver Username"