from django import forms

class Reg_Forms(forms.Form):
    username = forms.CharField(max_length=30, label='Your nick', required=True)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, label='Your password', required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, min_length=8, label='Confirm password', required=True)
    age = forms.CharField(max_length=3, label='Your age', required=True)
