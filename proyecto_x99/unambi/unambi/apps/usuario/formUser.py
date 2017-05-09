from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label = 'Usuario', max_length = 30)
    password = forms.CharField(label = 'Contraseña', max_length = 30, widget = forms.PasswordInput())


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password', 'email']
        help_texts={
            'username': '',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }