from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Enter User name',
            'password': 'Enter Password',
        }
        widgets = {
            'password': forms.PasswordInput()
        }


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ['username', 'email']
        # exclude = ['password1', 'password2']
        labels = {
            'username': 'Enter User name',
            'email': "Enter Email Address",
            'password': 'Enter Password',
        }
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput()
        }
