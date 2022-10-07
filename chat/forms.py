from cProfile import label
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='username',required=True, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput,required=True, label='password',max_length=32)