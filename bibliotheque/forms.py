from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Livre

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre','auteur','isbn','date_publication']
        widgets = {
            'date_publication' : forms.DateInput(attrs = {'type' : 'date'}),
        }