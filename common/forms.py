from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    first_name = User.first_name
    last_name = User.last_name

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
