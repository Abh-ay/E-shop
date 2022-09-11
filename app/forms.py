import email
from e_shopper import settings
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.contrib.auth import logout, login, authenticate


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=250, help_text='Must Be Valid E-Mail.')

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'E-Mail {email} Is Already Exists.')


# class LoginForm(forms.ModelForm):
#     password = forms.CharField(label='password', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('email', 'password')

#     def save(self, request):
#         email = self.cleaned_data['email']
#         password = self.cleaned_data['password']
#         account = authenticate(email=email, password=password)
#         if account:
#             login(request, account)

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
