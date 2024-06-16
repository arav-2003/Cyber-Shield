from django import forms

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=255)
    dob= forms.CharField(max_length=255)
    phone_number= forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password  = forms.CharField(max_length=255)

class LoginForm(forms.Form):
    email = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)