from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label='username', required=False)
    password = forms.CharField(min_length= 8, max_length=50, label='password', widget=forms.PasswordInput)
    email = forms.EmailField(label='email')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('This user already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('This email is already used')
        return email

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='username')
    password = forms.CharField(min_length= 8, max_length=50, label='password', widget=forms.PasswordInput)
