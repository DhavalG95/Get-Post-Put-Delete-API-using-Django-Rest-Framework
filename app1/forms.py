from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    surname = forms.CharField(max_length=101)
    email = forms.EmailField()
    number = forms.IntegerField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'surname', 'email', 'number','password1', 'password2']


class Info(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"